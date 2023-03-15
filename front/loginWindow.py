from PySide2.QtWidgets import *
import sys

from front.UI.mainscene import Ui_MainScene

sys.path.append("C:/Users/86177/PycharmProjects/Dva")


class LoginWindow(QMainWindow, Ui_MainScene):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.login_btn.clicked.connect(self.startWindow)

    def startWindow(self):
        from front.disWindow import ds
        ds.show()
        self.hide()
