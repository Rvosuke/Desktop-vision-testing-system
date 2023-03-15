# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CView(object):
    def setupUi(self, CView):
        if not CView.objectName():
            CView.setObjectName(u"CView")
        CView.resize(390, 844)
        CView.setMinimumSize(QSize(390, 844))
        CView.setMaximumSize(QSize(390, 844))
        self.toolButton_5 = QToolButton(CView)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(0, 0, 60, 60))
        self.toolButton_5.setMinimumSize(QSize(60, 60))
        self.toolButton_5.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setPointSize(12)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setAutoRaise(True)
        self.jilu = QWidget(CView)
        self.jilu.setObjectName(u"jilu")
        self.jilu.setGeometry(QRect(50, 530, 291, 101))
        self.formLayout = QFormLayout(self.jilu)
        self.formLayout.setObjectName(u"formLayout")
        self.log = QLabel(self.jilu)
        self.log.setObjectName(u"log")
        self.log.setMinimumSize(QSize(0, 50))
        self.log.setMaximumSize(QSize(16777215, 50))
        self.log.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.log)

        self.point = QLabel(self.jilu)
        self.point.setObjectName(u"point")
        self.point.setMinimumSize(QSize(100, 50))
        self.point.setMaximumSize(QSize(16777215, 50))
        self.point.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.point)

        self.fina = QLabel(CView)
        self.fina.setObjectName(u"fina")
        self.fina.setGeometry(QRect(130, 390, 111, 51))
        self.fina.setFont(font)

        self.retranslateUi(CView)

        QMetaObject.connectSlotsByName(CView)
    # setupUi

    def retranslateUi(self, CView):
        CView.setWindowTitle(QCoreApplication.translate("CView", u"\u89c6\u529b\u6d4b\u8bd5", None))
        self.toolButton_5.setText(QCoreApplication.translate("CView", u"\u8fd4\u56de", None))
        self.log.setText(QCoreApplication.translate("CView", u"<html><head/><body><p><span style=\" font-size:16pt;\">TextLabel</span></p></body></html>", None))
        self.point.setText(QCoreApplication.translate("CView", u"<html><head/><body><p><span style=\" font-size:16pt;\">TextLabel</span></p></body></html>", None))
        self.fina.setText(QCoreApplication.translate("CView", u"\u6d4b\u8bd5\u5b8c\u6bd5", None))
    # retranslateUi

