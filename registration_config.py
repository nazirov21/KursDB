# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reg(object):
    def setupUi(self, Reg):
        Reg.setObjectName("Reg")
        Reg.resize(400, 295)
        self.label = QtWidgets.QLabel(Reg)
        self.label.setGeometry(QtCore.QRect(180, 10, 81, 16))
        self.label.setObjectName("label")
        self.login = QtWidgets.QLineEdit(Reg)
        self.login.setGeometry(QtCore.QRect(190, 60, 131, 20))
        self.login.setText("")
        self.login.setObjectName("login")
        self.label_2 = QtWidgets.QLabel(Reg)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pwd = QtWidgets.QLineEdit(Reg)
        self.pwd.setGeometry(QtCore.QRect(190, 100, 131, 20))
        self.pwd.setText("")
        self.pwd.setObjectName("pwd")
        self.label_3 = QtWidgets.QLabel(Reg)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.reg_reg = QtWidgets.QPushButton(Reg)
        self.reg_reg.setGeometry(QtCore.QRect(140, 210, 131, 23))
        self.reg_reg.setObjectName("reg_reg")
        self.enter_reg = QtWidgets.QPushButton(Reg)
        self.enter_reg.setGeometry(QtCore.QRect(160, 250, 91, 23))
        self.enter_reg.setObjectName("enter_reg")
        self.label_4 = QtWidgets.QLabel(Reg)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 81, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Reg)
        self.label_5.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.label_5.setObjectName("label_5")
        self.r_pwd = QtWidgets.QLineEdit(Reg)
        self.r_pwd.setGeometry(QtCore.QRect(190, 150, 131, 20))
        self.r_pwd.setText("")
        self.r_pwd.setObjectName("r_pwd")

        self.retranslateUi(Reg)
        QtCore.QMetaObject.connectSlotsByName(Reg)

    def retranslateUi(self, Reg):
        _translate = QtCore.QCoreApplication.translate
        Reg.setWindowTitle(_translate("Reg", "Form"))
        self.label.setText(_translate("Reg", "Регистрация"))
        self.label_2.setText(_translate("Reg", "Логин:"))
        self.label_3.setText(_translate("Reg", "Пароль:"))
        self.reg_reg.setText(_translate("Reg", "Зарегестрироваться"))
        self.enter_reg.setText(_translate("Reg", "Вход"))
        self.label_5.setText(_translate("Reg", "Повторите пароль: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reg = QtWidgets.QWidget()
    ui = Ui_Reg()
    ui.setupUi(Reg)
    Reg.show()
    sys.exit(app.exec_())