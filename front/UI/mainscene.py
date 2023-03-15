# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainscene.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainScene(object):
    def setupUi(self, MainScene):
        if not MainScene.objectName():
            MainScene.setObjectName(u"MainScene")
        MainScene.resize(390, 844)
        MainScene.setMinimumSize(QSize(390, 844))
        MainScene.setMaximumSize(QSize(390, 844))
        self.centralwidget = QWidget(MainScene)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_title = QLabel(self.centralwidget)
        self.main_title.setObjectName(u"main_title")
        self.main_title.setGeometry(QRect(-10, 139, 400, 191))
        self.main_title.setMinimumSize(QSize(400, 50))
        self.main_title.setMaximumSize(QSize(400, 200))
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        self.main_title.setFont(font)
        self.main_title.setFrameShape(QFrame.WinPanel)
        self.login_btn = QToolButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(0, 480, 391, 61))
        font1 = QFont()
        font1.setPointSize(18)
        self.login_btn.setFont(font1)
        self.login_btn.setPopupMode(QToolButton.DelayedPopup)
        self.login_btn.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.login_btn.setAutoRaise(True)
        self.login_btn.setArrowType(Qt.NoArrow)
        MainScene.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainScene)

        QMetaObject.connectSlotsByName(MainScene)
    # setupUi

    def retranslateUi(self, MainScene):
        MainScene.setWindowTitle(QCoreApplication.translate("MainScene", u"VFD\u767b\u5f55", None))
        self.main_title.setText(QCoreApplication.translate("MainScene", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:400;\">\u6b22\u8fce\u4f7f\u7528</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:400;\">\u89c6\u529f\u80fd\u68c0\u6d4b</span></p></body></html>", None))
        self.login_btn.setText(QCoreApplication.translate("MainScene", u"\u8fdb\u5165", None))
    # retranslateUi

