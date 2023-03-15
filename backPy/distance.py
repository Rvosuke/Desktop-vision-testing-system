# distance.py
"""
距离检测模块
Rvosuke
start：2022/11/4 11：56
利用单目测距原理，对象为身份证类卡片，需要已知相机的焦距，返回距离（英寸）
1.对照片进行手部追踪/n
2.锁定手部的最小矩形/n
3.利用最小矩形对照片进行裁切/n
4.在裁切后的照片中进行轮廓检测卡片/n
5.找到卡片的四个角点并返回/n--利用霍夫变换求得卡片的直线
6.利用四个角点求出卡片的像素长和宽/n--处理直线族得到卡片短边长度
7.利用单目测距公式来求出卡片距离
Qs：对于目前收集拍摄的照片，体积太大。处理时间太长怎么办。
"""
import cv2  # 导入Opencv库
import hands
import numpy as np


def handCrop(IMAGE: np.array([]), Multiple: float = 2.7) -> list[np.array([])]:
    """
    返回一个裁切好的图片,传入参数表示找到手部多大的周围
    1.如何扩充裁切的范围--利用ndarray广播乘以裁切点集×
        通过单应性矩阵来扩大四个点框选图片的范围×
        现在已知四个点以及中心点，通过遍历四个点与中心点之间的距离来扩大（已解决）
    2.具体步骤
    调用hand_position获取手部点位，
    制作最小矩形，
    根据矩形对图片进行仿射变换，
    使矩形旋转到横向，
    根据中心点和四个角点扩大矩形，
    利用矩形对图片进行裁剪，
    返回值为cv2的图片类型。
    """
    hand_poss = hands.hand_positions(IMAGE, 0.3, 0.3)
    crop_img = []
    for hand_pos in hand_poss:
        hand_rect = cv2.minAreaRect(hand_pos)
        box_origin = np.int0(cv2.boxPoints(hand_rect))

        # cv2.drawContours(IMAGE, [box_origin], 0, (255, 0, 0), 20)
        # cv2.imwrite("最小外接矩形.jpg", IMAGE)
        # 构造旋转矩阵    旋转中心：矩形中心； 旋转角度； 缩放比例
        rot_M = cv2.getRotationMatrix2D(hand_rect[0], hand_rect[2], 1)
        dst = cv2.warpAffine(IMAGE, rot_M, (2 * IMAGE.shape[0], 2 * IMAGE.shape[1]))  # 进行仿射变换

        box = Rotate_cordite(hand_rect[2], box_origin, hand_rect[0][0], hand_rect[0][1])
        for i in range(4):
            box[i][0] = Multiple * box[i][0] - (Multiple - 1) * hand_rect[0][0]
            box[i][1] = Multiple * box[i][1] - (Multiple - 1) * hand_rect[0][1]
        box = np.int0(box)
        crop_img.append(imagecrop(dst, box))
    return crop_img


def imagecrop(IMAGE: np.array([]), BOX: list) -> np.array([]):
    xs = [x[1] for x in BOX]
    ys = [x[0] for x in BOX]
    cropimage = IMAGE[min(xs):max(xs), min(ys):max(ys)]
    return cropimage


# 逆时针旋转
def NRotate(angle, XValue, YValue, XPoint, YPoint):
    angle = (angle / 180) * np.pi
    XValue = np.array(XValue)
    YValue = np.array(YValue)
    nxRotate = (XValue - XPoint) * np.cos(angle) - (YValue - YPoint) * np.sin(angle) + XPoint
    nyRotate = (XValue - XPoint) * np.sin(angle) + (YValue - YPoint) * np.cos(angle) + YPoint
    return [nxRotate, nyRotate]


# 顺时针旋转
def SRotate(angle, XValue, YValue, XPoint, YPoint):
    """传入一个弧度角"""
    angle = (angle / 180) * np.pi
    XValue = np.array(XValue)
    YValue = np.array(YValue)
    sxRotate = (XValue - XPoint) * np.cos(angle) + (YValue - YPoint) * np.sin(angle) + XPoint
    syRotate = (YValue - YPoint) * np.cos(angle) - (XValue - XPoint) * np.sin(angle) + YPoint
    return [sxRotate, syRotate]  # 返回值为一个列表


# 将四个点做映射
def Rotate_cordite(angle, rectBoxs, XPoint, YPoint):
    """对矩形的四个顶点进行映射，将其映射为旋转后的四个点，放入到一个列表中"""
    output = []
    for rectBox in rectBoxs:
        if angle > 0:
            output.append(SRotate(angle, rectBox[0], rectBox[1], XPoint, YPoint))
        else:
            output.append(NRotate(-angle, rectBox[0], rectBox[1], XPoint, YPoint))
    return output


def find_card(IMAGES: list[np.array([])]) -> np.array([]):
    """定义目标函数，返回值为int（像素）"""
    images = handCrop(IMAGES)
    dis = -1
    for image in images:
        image = cv2.pyrMeanShiftFiltering(image, 25, 10)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将彩色图转化为灰度图
        ret, ts_img = cv2.threshold(gray_img, 170, 255, 0)
        # cv2.imwrite("二值化处理.jpg", ts_img)
        edged_img = cv2.Canny(ts_img, 90, 200)  # Canny算子阈值化
        # cv2.imwrite("轮廓检测.jpg", edged_img)
        lines = cv2.HoughLines(edged_img, 1, np.pi / 180, 55)  # 进行霍夫变换的直线检测
        rhoL = np.zeros(shape=[lines.shape[0], lines.shape[0], 2], order='C')
        num = []
        for i in range(lines.shape[0]):
            num.append(0)
        j = 0  # 直线族数
        # 建立直线族

        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * a)
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * a)

                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            line = np.squeeze(line)
            # line = line.tolist()

            b = True
            for i in range(j):
                if rhoL[i][1][0] - 10 <= line[0] <= rhoL[i][1][0] + 10:  # 加减像素值要根据图像来判断
                    num[i] += 1
                    rhoL[i][num[i]][0] = line[0]
                    rhoL[i][num[i]][1] = line[1]
                    b = False
            if b:
                if not num[j]:
                    num[j] = 1  # 在每个rho列表中的第一个空间存放该族的长度和序号
                    rhoL[j][num[j]][0] = line[0]
                    rhoL[j][num[j]][1] = line[1]
                    j += 1
        # 取直线族的均值
        rhoE = []
        thetaE = []
        for i in range(j):
            s1 = 0
            s2 = 0
            for rho, theta in rhoL[i]:
                s1 += rho
                s2 += theta
            s1 /= num[i]
            rhoE.append(s1)
            s2 /= num[i]
            thetaE.append(s2)

        for i in range(j):
            for x in range(i + 1, j):
                if abs(thetaE[x] - thetaE[i]) <= 0.1:  # 角度的阈值设定
                    dis = abs(rhoE[i] - rhoE[x])
    cv2.imwrite("直线检测.jpg", image)

    return dis


def distance_to_camera(knownWidth, focalLength, perWidth):
    """定义距离函数"""
    return (knownWidth * focalLength) / perWidth


def distance(IMAGE, FOCAL_LENGTH=35):
    """输入相机焦距，输出目标距离，取手机相机的等效焦距为24mm"""
    known_width = 85.6  # 已知物体的高度 （毫米）
    KNOWN_HEIGHT = 54  # 已知物体的宽度
    marker = find_card(IMAGE)
    distance = distance_to_camera(KNOWN_HEIGHT, FOCAL_LENGTH, marker)
    return distance * 10  # 返回值单位厘米


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    img = cv2.imread("res/imgX2.jpg")
    img = hands.img_resize(img)
    find_card(img)
    end = time.perf_counter()
    print(end - start)
    exit()
