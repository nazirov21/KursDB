# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clients.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clients(object):
    def setupUi(self, Clients):
        Clients.setObjectName("Clients")
        Clients.resize(437, 393)
        self.id_cl = QtWidgets.QLineEdit(Clients)
        self.id_cl.setGeometry(QtCore.QRect(160, 40, 81, 20))
        self.id_cl.setText("")
        self.id_cl.setObjectName("id_cl")
        self.name_cl = QtWidgets.QLineEdit(Clients)
        self.name_cl.setGeometry(QtCore.QRect(161, 70, 81, 20))
        self.name_cl.setText("")
        self.name_cl.setObjectName("name_cl")
        self.fam_cl = QtWidgets.QLineEdit(Clients)
        self.fam_cl.setGeometry(QtCore.QRect(161, 100, 81, 20))
        self.fam_cl.setText("")
        self.fam_cl.setObjectName("fam_cl")
        self.mail_cl = QtWidgets.QLineEdit(Clients)
        self.mail_cl.setGeometry(QtCore.QRect(161, 130, 81, 20))
        self.mail_cl.setText("")
        self.mail_cl.setObjectName("mail_cl")
        self.num_cl = QtWidgets.QLineEdit(Clients)
        self.num_cl.setGeometry(QtCore.QRect(161, 160, 81, 20))
        self.num_cl.setText("")
        self.num_cl.setObjectName("num_cl")
        self.label = QtWidgets.QLabel(Clients)
        self.label.setGeometry(QtCore.QRect(200, 10, 61, 21))
        self.label.setObjectName("label")
        self.add_cl = QtWidgets.QPushButton(Clients)
        self.add_cl.setGeometry(QtCore.QRect(260, 50, 75, 23))
        self.add_cl.setObjectName("add_cl")
        self.del_cl = QtWidgets.QPushButton(Clients)
        self.del_cl.setGeometry(QtCore.QRect(260, 90, 75, 23))
        self.del_cl.setObjectName("del_cl")
        self.back_cl = QtWidgets.QPushButton(Clients)
        self.back_cl.setGeometry(QtCore.QRect(260, 130, 75, 23))
        self.back_cl.setObjectName("back_cl")
        self.label_2 = QtWidgets.QLabel(Clients)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Clients)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Clients)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Clients)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Clients)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 111, 16))
        self.label_6.setObjectName("label_6")
        self.logs = QtWidgets.QTextEdit(Clients)
        self.logs.setGeometry(QtCore.QRect(10, 190, 421, 191))
        self.logs.setObjectName("logs")

        self.retranslateUi(Clients)
        QtCore.QMetaObject.connectSlotsByName(Clients)

    def retranslateUi(self, Clients):
        _translate = QtCore.QCoreApplication.translate
        Clients.setWindowTitle(_translate("Clients", "Form"))
        self.label.setText(_translate("Clients", "Клиенты"))
        self.add_cl.setText(_translate("Clients", "Добавить"))
        self.del_cl.setText(_translate("Clients", "Удалить"))
        self.back_cl.setText(_translate("Clients", "Назад"))
        self.label_2.setText(_translate("Clients", "ID клиента"))
        self.label_3.setText(_translate("Clients", "Имя"))
        self.label_4.setText(_translate("Clients", "Фамилия"))
        self.label_5.setText(_translate("Clients", "Email"))
        self.label_6.setText(_translate("Clients", "Номер телефона"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clients = QtWidgets.QWidget()
    ui = Ui_Clients()
    ui.setupUi(Clients)
    Clients.show()
    sys.exit(app.exec_())
