import csv
import time
import sys

import numpy as np
from PySide2.QtWidgets import *
from front.UI.distance import Ui_Distance

sys.path.append("C:/Users/86177/PycharmProjects")


localT = time.strftime('%y-%m-%d %H:%M', time.localtime())


class DisWindow(QWidget, Ui_Distance):

    def __init__(self):
        super(DisWindow, self).__init__()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.backWindow)
        self.toolButton_2.clicked.connect(self.startWindow2)
        self.toolButton_3.clicked.connect(self.startWindow1)

    def backWindow(self):
        # from Dva.front.baseWindow import bw
        # bw.show()
        # self.hide()
        pass

    def startWindow1(self):
        self.hide()
        from front import cWindow2
        cWindow2.distance = 2
        c3 = cWindow2.c3
        c3.fina.hide()
        while c3.High() - c3.Low() >= 0.1:
            c3.show()
            c3.judgeNear(0.5, 0.3, 2)
        c3.fina.show()
        c3.log.setText(f'五分结果：{round(c3.L, 1)}')
        c3.point.setText(f'小数结果：{round(c3.V, 1)}')
        data = np.array([c3.L, c3.V, localT, "Far"])
        with open('record.csv', 'a', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()
        c3.refresh(2)

    def startWindow2(self):
        self.hide()
        from front import cWindow2
        c2 = cWindow2.c2
        c2.fina.hide()
        c2.distance = 0.6
        while c2.High() - c2.Low() >= 0.05:
            c2.show()
            c2.judgeNear(0.5, 0.1, 0.5)
        c2.fina.show()
        c2.log.setText(f'五分结果：{round(c2.L, 1)}')
        c2.point.setText(f'小数结果：{round(c2.V, 1)}')
        data = np.array([c2.L, c2.V, localT, "Near"])
        with open('record.csv', 'a', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()
        c2.refresh(0.5)


ds = DisWindow()
