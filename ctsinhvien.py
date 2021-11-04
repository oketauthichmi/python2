# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctsinhvien.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_MainCTSV(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 121, 31))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(220, 40, 191, 31))
        self.name.setText("")
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 121, 31))
        self.label_2.setObjectName("label_2")
        self.sdt = QtWidgets.QLabel(self.centralwidget)
        self.sdt.setGeometry(QtCore.QRect(220, 110, 191, 31))
        self.sdt.setText("")
        self.sdt.setObjectName("sdt")
        self.show = QtWidgets.QPushButton(self.centralwidget)
        self.show.setGeometry(QtCore.QRect(700, 30, 91, 31))
        self.show.setObjectName("show")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 201, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 390, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 470, 181, 31))
        self.label_7.setObjectName("label_7")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(220, 180, 191, 31))
        self.email.setText("")
        self.email.setObjectName("email")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(220, 250, 191, 31))
        self.address.setText("")
        self.address.setObjectName("address")
        self.CCCD = QtWidgets.QLabel(self.centralwidget)
        self.CCCD.setGeometry(QtCore.QRect(220, 320, 191, 31))
        self.CCCD.setText("")
        self.CCCD.setObjectName("CCCD")
        self.birday = QtWidgets.QLabel(self.centralwidget)
        self.birday.setGeometry(QtCore.QRect(220, 390, 191, 31))
        self.birday.setText("")
        self.birday.setObjectName("birday")
        self.chuyennganh = QtWidgets.QLabel(self.centralwidget)
        self.chuyennganh.setGeometry(QtCore.QRect(220, 470, 191, 31))
        self.chuyennganh.setText("")
        self.chuyennganh.setObjectName("chuyennganh")
        self.updatett = QtWidgets.QPushButton(self.centralwidget)
        self.updatett.setGeometry(QtCore.QRect(630, 110, 93, 28))
        self.updatett.setObjectName("updatett")
        self.masv = QtWidgets.QComboBox(self.centralwidget)
        self.masv.setGeometry(QtCore.QRect(530, 40, 121, 22))
        self.masv.setMaxCount(2147483640)
        self.masv.setObjectName("masv")
        self.masv.addItem("")
        self.checkmasv()
        dem=0
        for i in self.row:
            i=list(i)
            #print(i)
            dem = dem+1
            self.masv.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(480, 170, 391, 341))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(0, 170, 181, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 121, 31))
        self.label_11.setObjectName("label_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 170, 191, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(220, 250, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show.clicked.connect(self.backendctsv)
        self.updatett.clicked.connect(self.updatectsv)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Tên sinh viên</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Số điện thoại</span></p></body></html>"))
        self.show.setText(_translate("MainWindow", "show"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Email</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Địa chỉ</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Số căn cước công dân</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Ngày sinh</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Chuyên ngành học</span></p></body></html>"))
        self.updatett.setText(_translate("MainWindow", "sửa thông tin"))
        self.masv.setCurrentText(_translate("MainWindow", "--SELECT--"))
        self.masv.setItemText(0, _translate("MainWindow", "--SELECT--"))
        self.groupBox.setTitle(_translate("MainWindow", "update"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">số điện thoại</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Địa chỉ</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Căn cước công dân</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Ngày sinh</span></p></body></html>"))
        self.checkmasv()
        dem=0
        for i in self.row:
            i=list(i)
            #print(i)
            dem = dem+1
            self.masv.setItemText(dem, _translate("MainWindow", str(i[0])))
            #print(dem)
    def checkmasv(self):
        self.conn = sqlite3.connect("E:/bc/ktpython.db")
        query = "SELECT masv FROM chitiet"
        self.curor = self.conn.execute(query)
        self.row = self.curor.fetchall()
        return self.row
        #print(len(self.row))
        #for i in self.row:
            #print(i)
    def backendctsv(self):
        masv = self.masv.currentText()
        self.conn = sqlite3.connect("E:/bc/ktpython.db")
        if masv=='--SELECT--':
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("Chọn mã sinh viên")
        else:
            query = "SELECT * FROM chitiet WHERE masv="+str(masv)
            self.curor = self.conn.execute(query)
            self.row = self.curor.fetchall()
            for i in self.row:
                i=list(i)
                self.name.setText(str(i[1]))
                self.sdt.setText(str(i[2]))
                self.email.setText(str(i[3]))
                self.address.setText(str(i[4]))
                self.CCCD.setText(str(i[5]))
                self.birday.setText(str(i[6]))
                self.chuyennganh.setText(str(i[7]))
    def updatectsv(self):
        masv = self.masv.currentText()
        sdt = self.lineEdit.text()
        cccd = self.lineEdit_3.text()
        diachi = self.lineEdit_2.text()
        ngaysinh = self.dateEdit.text()
        self.conn = sqlite3.connect("E:/bc/ktpython.db")
        if sdt=='' or cccd == '' or diachi=='':
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("Vui lòng nhập đầy đủ thông tin")
        elif sdt.isnumeric() == False:
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("Nhập chính xác số điện thoại")
        elif cccd.isnumeric() == False:
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage("Nhập chính xác số căn cước của bạn")
        else:
            query = "UPDATE chitiet SET sdt=?, address=?, cccd=?, ngaysinh=? WHERE masv=?"
            data = (sdt,diachi,cccd,ngaysinh,masv)
            self.conn.execute(query,data)
            self.conn.commit()
            self.conn.close()
            self.backendctsv()
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("cập nhập thành công")
            self.msg.setWindowTitle("Thành công")
            self.msg.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainCTSV()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
