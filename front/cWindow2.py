"""
视力测试的界面，与远视力测试界面相同，但是内部机制和运行逻辑有所不同，具体如下：
在进入界面后假定已经确定好了测试距离为40cm，直接显示一张C字图片，40cm处的5.0 C字大小为————（需要进行计算）
# 用户需要在3秒内进行判定，点击某个按钮即表示确定方向×
若在3秒内没有进行判定，则认定为判断错误
"""
import ctypes
import math
import random
import sys

from backPy.hands import judge_direction
from PySide2.QtCore import QRectF
from PySide2.QtGui import QPainterPath, QColor, QPen, QPainter, QPaintEvent
from PySide2.QtWidgets import QWidget
from front.UI.cview import Ui_CView

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
LOGPIXELSX = 88
LOGPIXELSY = 90

user32.SetProcessDPIAware()
hDC = user32.GetDC(0)
hdpi = gdi32.GetDeviceCaps(hDC, LOGPIXELSX)
ydpi = gdi32.GetDeviceCaps(hDC, LOGPIXELSY)
# print(hdpi, ydpi)


preJudge = -1
preD = 4
high = 1
low = 0


class CWindow2(QWidget, Ui_CView):
    userD = 0  # 用户给出的方向
    # 选定的测试距离 单位m
    D = 3  # 当前视标的设计距离
    a = 2 * math.atan(math.tan(1 / 120 * math.pi / 180) * D / 3)  # 当前视标的视角
    w = 2 * 3 * math.tan(a / 2)  # 视标参数，即缺口大小 此处计算得到的单位为m，而绘制时单位为px
    V = 3 / D  # 小数记录法
    L = 5 + math.log10(V)  # 五分记录法

    vision = 1 / a  # 用户的视力情况，保存到数据库中
    scenery_direction = 3  # 屏幕中显示的视标的方向 1：下  2：左  3：上  4：右

    def __init__(self, dis):
        super(CWindow2, self).__init__()
        self.refresh(dis)
        self.setupUi(self)
        self.fina.hide()
        self.toolButton_5.clicked.connect(self.backWindow)
        self.log.setText(f'五分记录：{self.L:.2f}')
        self.point.setText(f'小数记录：{self.V:.2f}')

    def High(self):
        global high
        return high

    def Low(self):
        global low
        return low

    def backWindow(self):
        from front.disWindow import ds
        ds.show()
        self.close()

    def setDirection(self):
        self.scenery_direction = random.randint(1, 4)

    def paintEvent(self, event=QPaintEvent):
        """
        在本函数中要设置一个3秒判断的事件：若在3秒内没有进行任何操作，则自动更新画面并且wrongNum++
        思路1：建立多线程来设置一个时间循环，但是时间循环会独立于按键之外
        思路2：直接在本函数中设置一个时间循环，但是本函数可能会导致程序断点
        :param event:在开启界面时自动运行，在调用self.update函数也会运行
        :return: 根据当前的w和d来绘制一个c字
        """
        global hdpi
        w = (self.w * 1000 / 25.4) * hdpi
        self.setDirection()
        d = self.scenery_direction
        painter = QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing)  # 平滑处理

        # 绘制圆
        pen1 = QPen()
        pen1.setWidthF(w)
        painter.setPen(pen1)
        rect = QRectF(195 - 2 * w, 195 - 2 * w, 4 * w, 4 * w)
        painter.drawEllipse(rect)
        # 绘制缺口的矩形
        pen2 = QPen()
        pen2.setColor(QColor(238, 238, 238))
        painter.setPen(pen2)
        path = QPainterPath()

        if d == 1:
            path.addRect(QRectF(195 - w / 2, 195 + 2 * w - w / 2 - w / 8, w, w + w / 4))
        if d == 2:
            path.addRect(QRectF(195 - 2 * w - w / 2 - w / 8, 195 - w / 2, w + w / 4, w))
        if d == 3:
            path.addRect(QRectF(195 - w / 2, 195 - 2 * w - w / 2 - w / 8, w, w + w / 4))
        if d == 4:
            path.addRect(QRectF(195 + 2 * w - w / 2 - w / 8, 195 - w / 2, w + w / 4, w))
        painter.fillPath(path, QColor(238, 238, 238))
        painter.drawPath(path)

    def judgeNear(self, difP, difC, dis):
        """
        方向选择正确与否的判断
        若判断正确，则正确记录加一，并缩小w
        否则增加w
        :return: void
        """
        global preD, preJudge, high, low

        # thread.start_new_thread(judge_direction(self.scenery_direction), ("Thread-1", 2,))
        nowJudge = judge_direction(self.scenery_direction)
        print(nowJudge)
        if preJudge == -1:  # 第一次进行判断
            preD = self.D
            if nowJudge:
                self.D -= difC
            else:
                self.D += difP
            preJudge += 1
        elif nowJudge == preJudge and not preJudge == 3:  # 如果连续判断错误
            preD = self.D
            if nowJudge:
                self.D -= difC
            else:
                self.D += difP
            preJudge = nowJudge
        elif not preJudge == 3:
            preJudge = 3
            if self.D > preD:
                low = preD
                high = self.D
            else:
                low = self.D
                high = preD
            self.D = (low + high) / 2

        elif preJudge == 3:
            if nowJudge:
                high = self.D
            else:
                low = self.D
            self.D = (high + low) / 2
        print(high, low, high - low)
        self.record(dis)
        self.log.setText(f'五分记录：{self.L:.2f}')
        self.point.setText(f'小数记录：{self.V:.2f}')
        # print(f'五分记录：{c2.L}')
        # print(f'小数记录：{c2.V}')

        self.repaint()

    def refresh(self, dis):
        global preJudge, low, high, preD
        self.userD = 0  # 用户给出的方向  # 选定的测试距离 单位m
        self.D = dis  # 当前视标的设计距离
        self.record(dis)
        self.scenery_direction = 3  # 屏幕中显示的视标的方向 1：下  2：左  3：上  4：右
        preJudge = -1
        preD = 4
        high = 1
        low = 0

    def record(self, dis):
        self.a = 2 * math.atan(math.tan(1 / 120 * math.pi / 180) * self.D / dis)  # 当前视标的视角
        self.w = 2 * dis * math.tan(self.a / 2)  # 视标参数，即缺口大小 此处计算得到的单位为m，而绘制时单位为px
        self.V = dis / self.D  # 小数记录法
        self.L = 5 + math.log10(self.V)  # 五分记录法
        self.vision = 1 / self.a  # 用户的视力情况，保存到数据库中


c2 = CWindow2(0.5)
c3 = CWindow2(3)

if __name__ == '__main__':
    pass
