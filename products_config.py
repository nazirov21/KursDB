# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Products.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Product(object):
    def setupUi(self, Product):
        Product.setObjectName("Product")
        Product.resize(471, 352)
        self.add_prod = QtWidgets.QPushButton(Product)
        self.add_prod.setGeometry(QtCore.QRect(320, 50, 91, 23))
        self.add_prod.setObjectName("add_prod")
        self.del_prod = QtWidgets.QPushButton(Product)
        self.del_prod.setGeometry(QtCore.QRect(320, 80, 91, 23))
        self.del_prod.setObjectName("del_prod")
        self.back_prod = QtWidgets.QPushButton(Product)
        self.back_prod.setGeometry(QtCore.QRect(320, 110, 91, 23))
        self.back_prod.setObjectName("back_prod")
        self.id_prod = QtWidgets.QLineEdit(Product)
        self.id_prod.setGeometry(QtCore.QRect(210, 30, 91, 20))
        self.id_prod.setText("")
        self.id_prod.setObjectName("id_prod")
        self.name_prod = QtWidgets.QLineEdit(Product)
        self.name_prod.setGeometry(QtCore.QRect(210, 60, 91, 20))
        self.name_prod.setText("")
        self.name_prod.setObjectName("name_prod")
        self.cap_prod = QtWidgets.QLineEdit(Product)
        self.cap_prod.setGeometry(QtCore.QRect(210, 90, 91, 20))
        self.cap_prod.setText("")
        self.cap_prod.setObjectName("cap_prod")
        self.price_prod = QtWidgets.QLineEdit(Product)
        self.price_prod.setGeometry(QtCore.QRect(210, 120, 91, 20))
        self.price_prod.setText("")
        self.price_prod.setObjectName("price_prod")
        self.id_cat = QtWidgets.QLineEdit(Product)
        self.id_cat.setGeometry(QtCore.QRect(210, 150, 91, 20))
        self.id_cat.setText("")
        self.id_cat.setObjectName("id_cat")
        self.label = QtWidgets.QLabel(Product)
        self.label.setGeometry(QtCore.QRect(210, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Product)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Product)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Product)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Product)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Product)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 131, 16))
        self.label_6.setObjectName("label_6")
        self.logs = QtWidgets.QTextEdit(Product)
        self.logs.setGeometry(QtCore.QRect(10, 180, 451, 161))
        self.logs.setObjectName("logs")

        self.retranslateUi(Product)
        QtCore.QMetaObject.connectSlotsByName(Product)

    def retranslateUi(self, Product):
        _translate = QtCore.QCoreApplication.translate
        Product.setWindowTitle(_translate("Product", "Form"))
        self.add_prod.setText(_translate("Product", "Добавить"))
        self.del_prod.setText(_translate("Product", "Удалить"))
        self.back_prod.setText(_translate("Product", "Назад"))
        self.label.setText(_translate("Product", "Продукты"))
        self.label_2.setText(_translate("Product", "ID продукта"))
        self.label_3.setText(_translate("Product", "Наименование товара"))
        self.label_4.setText(_translate("Product", "Описание продукта"))
        self.label_5.setText(_translate("Product", "Цена за единицу"))
        self.label_6.setText(_translate("Product", "ID категории"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Product = QtWidgets.QWidget()
    ui = Ui_Product()
    ui.setupUi(Product)
    Product.show()
    sys.exit(app.exec_())
