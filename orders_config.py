# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Order(object):
    def setupUi(self, Order):
        Order.setObjectName("Order")
        Order.resize(400, 317)
        self.add_o = QtWidgets.QPushButton(Order)
        self.add_o.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.add_o.setObjectName("add_o")
        self.del_o = QtWidgets.QPushButton(Order)
        self.del_o.setGeometry(QtCore.QRect(290, 60, 75, 23))
        self.del_o.setObjectName("del_o")
        self.label = QtWidgets.QLabel(Order)
        self.label.setGeometry(QtCore.QRect(180, 0, 41, 20))
        self.label.setObjectName("label")
        self.id_order = QtWidgets.QLineEdit(Order)
        self.id_order.setGeometry(QtCore.QRect(140, 20, 81, 20))
        self.id_order.setText("")
        self.id_order.setObjectName("id_order")
        self.id_client_o = QtWidgets.QLineEdit(Order)
        self.id_client_o.setGeometry(QtCore.QRect(140, 50, 81, 20))
        self.id_client_o.setText("")
        self.id_client_o.setObjectName("id_client_o")
        self.date_order_o = QtWidgets.QLineEdit(Order)
        self.date_order_o.setGeometry(QtCore.QRect(140, 80, 81, 20))
        self.date_order_o.setText("")
        self.date_order_o.setObjectName("date_order_o")
        self.price_o = QtWidgets.QLineEdit(Order)
        self.price_o.setGeometry(QtCore.QRect(140, 110, 81, 20))
        self.price_o.setText("")
        self.price_o.setObjectName("price_o")
        self.back_o = QtWidgets.QPushButton(Order)
        self.back_o.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.back_o.setObjectName("back_o")
        self.label_2 = QtWidgets.QLabel(Order)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Order)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Order)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Order)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_5.setObjectName("label_5")
        self.logs = QtWidgets.QTextEdit(Order)
        self.logs.setGeometry(QtCore.QRect(10, 140, 381, 171))
        self.logs.setObjectName("logs")

        self.retranslateUi(Order)
        QtCore.QMetaObject.connectSlotsByName(Order)

    def retranslateUi(self, Order):
        _translate = QtCore.QCoreApplication.translate
        Order.setWindowTitle(_translate("Order", "Form"))
        self.add_o.setText(_translate("Order", "Добавить "))
        self.del_o.setText(_translate("Order", "Удалить"))
        self.label.setText(_translate("Order", "Заказы"))
        self.back_o.setText(_translate("Order", "Назад"))
        self.label_2.setText(_translate("Order", "ID заказа"))
        self.label_3.setText(_translate("Order", "ID клиента"))
        self.label_4.setText(_translate("Order", "Дата заказа"))
        self.label_5.setText(_translate("Order", "Итоговая цена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Order = QtWidgets.QWidget()
    ui = Ui_Order()
    ui.setupUi(Order)
    Order.show()
    sys.exit(app.exec_())
