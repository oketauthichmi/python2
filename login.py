# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
from gdmain import Ui_MainWindow
from register import Ui_MainRegister


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 61, 31))
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(60, 140, 93, 28))
        self.login.setObjectName("login")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 140, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 200, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(150, 20, 113, 22))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 80, 113, 22))
        self.password.setObjectName("password")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.login.clicked.connect(self.checkuser)
        self.pushButton_2.clicked.connect(self.registerform)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "username"))
        self.label_2.setText(_translate("Dialog", "password"))
        self.login.setText(_translate("Dialog", "login"))
        self.pushButton_2.setText(_translate("Dialog", "register"))
        self.pushButton_3.setText(_translate("Dialog", "forget"))
    def checkuser(self,error):
        self.conn = sqlite3.connect("E:/bc/ktpython.db")
        query = "SELECT user,password FROM admin"
        curor = self.conn.execute(query)
        self.abc = curor.fetchall()
        ck = (self.username.text(),self.password.text())
        if ck in self.abc:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
        elif self.username.text() == '' or self.password.text()=='':
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("Vui lòng điền đầy đủ thông tin tài khoản!")
        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("thông tin tài khoản hoặc mật khẩu không chính xác!")
    def registerform(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainRegister()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
            
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
