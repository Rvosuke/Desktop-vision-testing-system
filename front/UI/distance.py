# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'distance.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Distance(object):
    def setupUi(self, Distance):
        if not Distance.objectName():
            Distance.setObjectName(u"Distance")
        Distance.resize(800, 844)
        Distance.setMinimumSize(QSize(389, 844))
        Distance.setMaximumSize(QSize(844, 844))
        self.toolButton = QToolButton(Distance)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(0, 0, 60, 60))
        self.toolButton.setMinimumSize(QSize(60, 60))
        self.toolButton.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setPointSize(12)
        self.toolButton.setFont(font)
        self.toolButton.setAutoRaise(True)
        self.toolButton_2 = QToolButton(Distance)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(200, 80, 400, 60))
        self.toolButton_2.setMinimumSize(QSize(400, 60))
        self.toolButton_2.setMaximumSize(QSize(400, 60))
        font1 = QFont()
        font1.setPointSize(16)
        self.toolButton_2.setFont(font1)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_3 = QToolButton(Distance)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(200, 170, 400, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMinimumSize(QSize(400, 60))
        self.toolButton_3.setFont(font1)
        self.toolButton_3.setAutoRaise(True)
        self.label = QLabel(Distance)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 230, 801, 611))
        font2 = QFont()
        font2.setPointSize(9)
        self.label.setFont(font2)

        self.retranslateUi(Distance)

        QMetaObject.connectSlotsByName(Distance)
    # setupUi

    def retranslateUi(self, Distance):
        Distance.setWindowTitle(QCoreApplication.translate("Distance", u"\u89c6\u529b\u6d4b\u8bd5", None))
        self.toolButton.setText(QCoreApplication.translate("Distance", u"\u8fd4\u56de", None))
        self.toolButton_2.setText(QCoreApplication.translate("Distance", u"\u8fd1\u89c6\u529b\u6d4b\u8bd5", None))
        self.toolButton_3.setText(QCoreApplication.translate("Distance", u"\u8fdc\u89c6\u529b\u6d4b\u8bd5", None))
        self.label.setText(QCoreApplication.translate("Distance", u"\u6b22\u8fce\u4f7f\u7528\u672c\u89c6\u529b\u68c0\u6d4b\u5de5\u5177\uff01\u5728\u8fdb\u884c\u6d4b\u8bd5\u524d\uff0c\u8bf7\u6ce8\u610f\u4ee5\u4e0b\u4e8b\u9879\uff1a\n"
"\u8bf7\u786e\u5b9a\u8981\u6d4b\u8bd5\u7684\u773c\u775b\uff0c\u5e76\u7528\u540c\u4fa7\u624b\u638c\u6342\u4f4f\u672a\u88ab\u6d4b\u7684\u540c\u4fa7\u773c\uff0c\u4ee5\u786e\u4fdd\u6d4b\u8bd5\u7ed3\u679c\u51c6\u786e\u3002\n"
"\u8bf7\u5728\u6b63\u5e38\u5149\u7ebf\u4e0b\u4f7f\u7528\u672c\u5de5\u5177\uff0c\u4ee5\u907f\u514d\u6d4b\u8bd5\u7ed3\u679c\u53d7\u5230\u5f71\u54cd\u3002\n"
"\u5f53\u6d4b\u8bd5\u65f6\uff0c\u8bf7\u52ff\u51fa\u73b0\u591a\u4eba\u624b\u638c\u5728\u6444\u50cf\u5934\u524d\uff0c\u4ee5\u786e\u4fdd\u6d4b\u8bd5\u7ed3\u679c\u51c6\u786e\u3002\n"
"\n"
"\u6d4b\u8bd5\u6b65\u9aa4\u5982\u4e0b\uff1a\n"
"\u70b9\u51fb\u201c\u89c6\u529b\u68c0\u6d4b\u201d\u6309\u94ae\uff0c\u5f00\u59cb\u6d4b\u8bd5\u3002\n"
"\u5f53\u51fa\u73b0C\u89c6\u6807\u540e\uff0c\u8bf7\u7528\u95f2\u7f6e\u624b\u7684\u98df\u6307\u4e0e\u4e2d\u6307\u4e00\u8d77\u6307\u51fa\u81ea\u5df1\u770b"
                        "\u5230\u7684\u7f3a\u53e3\u65b9\u5411\u3002\n"
"\u5982\u679c\u770b\u4e0d\u6e05\uff0c\u5219\u4e24\u5f20\u624b\u638c\u90fd\u5f20\u5f00\u3002\n"
"\u91cd\u590d\u4e0a\u8ff0\u64cd\u4f5c\uff0c\u76f4\u5230\u754c\u9762\u663e\u793a\u201c\u6d4b\u8bd5\u5b8c\u6bd5\u201d\u3002\n"
"\u67e5\u770b\u81ea\u5df1\u7684\u6d4b\u8bd5\u7ed3\u679c\u3002\n"
"\n"
"\u6ce8\u610f\u4e8b\u9879\uff1a\n"
"\u5982\u679c\u7cfb\u7edf\u8fde\u7eed\u591a\u6b21\u5224\u65ad\u9519\u8bef\uff0c\u8bf7\u91cd\u65b0\u8fdb\u884c\u6d4b\u8bd5\u3002\n"
"\n"
"\u5e0c\u671b\u672c\u4f7f\u7528\u8bf4\u660e\u80fd\u591f\u5e2e\u52a9\u60a8\u8fdb\u884c\u51c6\u786e\u7684\u89c6\u529b\u68c0\u6d4b\uff0c\u5982\u6709\u4efb\u4f55\u95ee\u9898\uff0c\u8bf7\u8054\u7cfb\u6211\u4eec\u7684\u5ba2\u670d\u3002", None))
    # retranslateUi

