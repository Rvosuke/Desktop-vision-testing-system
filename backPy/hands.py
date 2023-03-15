# hands.py
"""
手势识别模块
Rvosuke
start：2022/11/4 02：06
/n
计划使用mediapipe追踪的手部，根据其21个点位的不同位置来判断手势/n
具体步骤如下：/n
1.找到五根手指上边的点位/n
2.根据关节点位制作两点向量/n
3.取得最长的向量作为判断/n
4.判断最长向量在笛卡尔坐标系中成角来判断方向/n
5.将实时检测出来的方向取时间间隔来判断，如停留1秒钟/n
6.返回标准方向向量--返回bool/n
finish：2022/11/5 14：07

ps：11.12现在识别的手指为手的根部到指尖，故建议使用食指或中指来进行测试，切忌使用大拇指
         在有两个手出现在屏幕中，很容易误判另一只手，现在还没有进行优化。
"""

import cv2
import mediapipe as mp
import numpy as np
import time
import _thread


def img_resize(image):
    """
    重设图片的函数，将图片缩小为854*480，便于进行计算
    :param image:
    :return:
    """
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = 480
    height_new = 854
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new


def capture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    rat, img = cap.read()
    # img = img_resize(img)
    img = cv2.flip(img, 1)

    return img


def hand_positions(IMAGE, MinDC=0.2, MinTC=0.1):
    """
    输入已读取的图片，返回手部21个点位
    问题：
    1.如果识别到两个手部点位的情况，怎么同时返回两个手部点集数组--修改返回值为存放多个点集的列表（已解决）/n
    2.如果手部持卡，需要把手部追踪的严谨度调低，如何动态实现这一目标--修改形参（已解决）/n

    3.hand_positions只是在寻找手，不管是拳头还是手掌，此函数一直运行到捕捉到手为止，现在返回的是两只手
    MinDC:手的置信度
    MinTC:跟手性
    """
    imgRGB = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2RGB)  # 将图像格式设置为RGB
    mpHands = mp.solutions.hands  # 调用mediapipe库中的模板
    mp_drawing = mp.solutions.drawing_utils
    handLmsStyle = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
    handConStyle = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)

    hands = mpHands.Hands(min_detection_confidence=MinDC, min_tracking_confidence=MinTC)  # 设置手部追踪的严谨度
    result = hands.process(imgRGB)  # 使用mediapipe处理图片
    Pos_ls = []
    imgHeight = IMAGE.shape[0]  # 获取图像的高
    imgWidth = IMAGE.shape[1]  # 获取图像的宽
    if result.multi_hand_landmarks:
        """图像/坐标 处理"""
        for handLms in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(IMAGE, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)  # 显示线条
            Pos = np.array([])
            for i, lm in enumerate(handLms.landmark):
                """处理21个点坐标"""
                xPos = lm.x * imgWidth  # 图像的x坐标
                yPos = lm.y * imgHeight  # 图像的Y坐标
                p = [xPos, yPos]
                Pos = np.append(Pos, p, axis=0)
            Pos = np.resize(Pos, [21, 2])
            Pos = np.int0(Pos)  # 转化为像素坐标（整形）
            Pos_ls.append(Pos)
            cv2.imshow("capture", IMAGE)
            cv2.waitKey(1)
    else:
        text = "Can't Find Hands"
        cv2.putText(IMAGE, text, (int(imgWidth / 4), int(imgHeight / 2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        cv2.imshow("capture", IMAGE)
        cv2.waitKey(1)
        hand_positions(capture(), MinDC, MinTC)  # 这样是对当前的图片一直搜索手部，肯定是个死循环
    return Pos_ls


def find_finger(IMAGE):
    """
    1.输入一个图片，输出其最长的手指向量，函数中调用了hand_position
    2.此函数是为了找到手掌的手，如果找不到就一直找
    3.为了辨别出是否有手指指出，我们利用hand_positions的长度来判断有几个手
    4.如果只有一个手，则必须是手掌，因为我们需要手掌来捂住一个眼睛，这个要求要在进行近远距离测试选定的时候就要开始捂眼睛，确保有一个手会出现
    5.如果两只手，判断出来一个非手掌的手，将其手指向量进行返回
    """
    result = None
    poss = hand_positions(IMAGE)
    for pos in poss:
        var1 = np.array([pos[4][0] - pos[1][0], pos[4][1] - pos[1][1]])
        var2 = np.array([pos[8][0] - pos[5][0], pos[8][1] - pos[5][1]])
        var3 = np.array([pos[12][0] - pos[9][0], pos[12][1] - pos[9][1]])
        var4 = np.array([pos[16][0] - pos[13][0], pos[16][1] - pos[13][1]])
        var5 = np.array([pos[20][0] - pos[17][0], pos[20][1] - pos[17][1]])
        finger_vector = np.array([var1, var2, var3, var4, var5])

        norm = []  # 模长平方
        for i in finger_vector:
            norm.append(i[0] * i[0] + i[1] * i[1])

        n = max(norm)
        n = norm.index(n)  # 判断最长手指的序号
        count = 0
        for i in range(5):  # 判断手掌0：当至少有一个手指小于最长手指1/2时候认为就不是拳头
            if i != n and norm[n] < 4 * norm[i]:  # 误判:来判断是否其他手指长度大于最长的1/2，是则累计加一
                count += 1

        if len(poss) <= 1:  # 只识别出一只手或者没有识别出手的时候，提示用户伸出另一只手
            text = "Can't Find Fingers"
            cv2.putText(IMAGE, text, (int(IMAGE.shape[1] / 4), int(IMAGE.shape[0] / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            cv2.imshow("capture", IMAGE)
            cv2.waitKey(1)
            result = find_finger(capture())  # 对下一帧图形重新查找手指

        else:
            if count >= 4:  # 其他手指都大于，则是手掌
                result = None
            else:
                cv2.imshow("capture", IMAGE)
                cv2.waitKey(1)
                result = finger_vector[n]

    return result


def finger_direction(nd: np.array([])):
    """
    涉及到周期问题：在第一象限和第三象限输出的幅角相同--设置多个分支条件判断（已解决）
    """
    if nd is not None:
        y = nd[1]
        x = nd[0]
        if x == 0:
            x = 0.00001
        arg_rad = np.arctan(y / x)  # 返回值为弧度

        if nd[0] < 0 and nd[1] < 0:  # 第三象限
            arg_rad = np.pi + arg_rad
        elif nd[0] < 0 < nd[1]:  # 第二象限
            arg_rad = np.pi + arg_rad
        elif nd[0] > 0 > nd[1]:  # 第四象限
            arg_rad = 2 * np.pi + arg_rad
        # arg = arg_rad * 180 / np.pi

        e = np.pi / 4
        if (np.pi / 2 - e) <= arg_rad < (np.pi / 2 + e):
            return 1  # 下
        elif (np.pi - e) <= arg_rad < (np.pi + e):
            return 2  # 左
        elif (np.pi * 3 / 2 - e) <= arg_rad < (np.pi * 3 / 2 + e):
            return 3  # 上
        elif (np.pi * 2 - e) <= arg_rad or arg_rad < e:
            return 4  # 右
    return 0


def judge_direction(correct_D: int) -> bool:
    """判断方向正确与否的函数，当在一定时间内，连续正确，则返回true，时间到则返回false"""
    start = time.perf_counter()
    distance = 0.1  # 循环时间
    counter = 0  # 循环次数
    correct_c = 0  # 正确次数
    wrong_c = 0
    while distance < 10:
        end = time.perf_counter()
        distance = end - start
        diff_time = counter * 0.2 - distance
        if finger_direction(find_finger(capture())) == correct_D:
            correct_c += 1
            wrong_c = 0
        else:
            correct_c = 0
            wrong_c += 1
        if correct_c >= 2:
            return True
        if wrong_c >= 4:
            return False
        if diff_time > 0:
            time.sleep(diff_time)
        counter += 1
    return False


if __name__ == '__main__':
    # img2 = cv2.imread("img2.jpg")
    # _thread.start_new_thread(show_cap, (0.5, 0.4))
    # _thread.start_new_thread(judge_direction, (2,))

    print(judge_direction(2))
    print(judge_direction(3))

    # hand_positions(img)
    exit()
    # cv2.imwrite("res/setSize.jpg", img_resize(img))
    # finger_arg(find_finger(img2))
    # print(finger_direction(find_finger(img)))
