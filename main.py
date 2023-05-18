from PyQt5 import QtCore, QtGui, QtWidgets

from enter_config import Ui_Enter
from registration_config import Ui_Reg
from menu_config import Ui_Menu
from orderdetails_config import Ui_Ord_Det
from category_config import Ui_Category
from orders_config import Ui_Order
from products_config import Ui_Product
from MarketingResearches_config import Ui_Mar_Res
from clients_config import Ui_Clients

import sys
import sqlite3

db = sqlite3.connect('base.db')
sql = db.cursor()

app = QtWidgets.QApplication(sys.argv)
Enter = QtWidgets.QDialog()
ui = Ui_Enter()
ui.setupUi(Enter)
Enter.show()

def check():
	mail = ui.email.text()
	pass_email = ui.pass_email.text()
	
	sql.execute(f'SELECT Email FROM Admins WHERE Email = "{mail}"')
	if sql.fetchone() is None:
		reg()
	else:
		for i in sql.execute(f'SELECT Password FROM Admins WHERE Email = "{mail}"'):
			pwd = i[0]
		if str(pwd) == pass_email:
			Enter.close()
			menu()

def reg():
	global Reg
	Reg = QtWidgets.QWidget()
	ui = Ui_Reg()
	ui.setupUi(Reg)
	Enter.close()
	Reg.show()

	def check_reg():
		login = ui.login.text()
		pwd = ui.pwd.text()
		r_pwd = ui.r_pwd.text()

		sql.execute(f'SELECT Email FROM Admins WHERE Email = "{login}"')
		if sql.fetchone() is None:
			if str(pwd) == str(r_pwd):
				sql.execute(f'INSERT INTO Admins VALUES(?, ?)', (login, pwd))
				db.commit()
				Reg.close()
				menu()
			else:
				ui.login.setText('')
				ui.pwd.setText('')
				ui.r_pwd.setText('')
		else:
			check()

	ui.login.returnPressed.connect(check_reg)
	ui.pwd.returnPressed.connect(check_reg)
	ui.r_pwd.returnPressed.connect(check_reg)
	ui.reg_reg.clicked.connect(check_reg)

def ord_det():
	global Ord_Det 
	Ord_Det = QtWidgets.QWidget()
	ui = Ui_Ord_Det()
	ui.setupUi(Ord_Det)
	Menu.close()
	Ord_Det.show()
	ui.logs.setReadOnly(True)

	logs = 'ID дет заказа | ID заказа | ID продукта | Кол-во | Цена за ед.'
	sql.execute('''SELECT * from OrderDetails''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'
	ui.logs.setText(f'{logs}')

	def add_od():
		id_ord_det = ui.id_ord_det.text()
		id_order = ui.id_order.text()
		id_prod_o = ui.id_prod_o.text()
		count = ui.count.text()
		price = ui.price.text()

		if id_ord_det == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT order_detail_id FROM OrderDetails WHERE order_detail_id = "{id_ord_det}"')
			if sql.fetchone() is None:
				sql.execute(f'INSERT INTO OrderDetails VALUES(?, ?, ?, ?, ?)', (id_ord_det, id_order, id_prod_o, count, price))
				db.commit()

				logs = 'ID дет заказа | ID заказа | ID продукта | Кол-во | Цена за ед.'
				sql.execute('''SELECT * from OrderDetails''')
				for i in sql.fetchall():
					logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

				ui.id_ord_det.setText('')
				ui.id_order.setText('')
				ui.id_prod_o.setText('')
				ui.count.setText('')
				ui.price.setText('')
				ui.logs.setText(f'База данных обновлена!\n{logs}')
			else:
				ui.id_ord_det.setText('')
				ui.id_order.setText('')
				ui.id_prod_o.setText('')
				ui.count.setText('')
				ui.price.setText('')

	def del_od():
		id_ord_det = ui.id_ord_det.text()

		if id_ord_det == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute('''DELETE FROM OrderDetails WHERE order_detail_id = ?''', (id_ord_det,))
			db.commit()

			logs = 'ID дет заказа | ID заказа | ID продукта | Кол-во | Цена за ед.'
			sql.execute('''SELECT * from OrderDetails''')
			for i in sql.fetchall():
				logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

			ui.id_ord_det.setText('')
			ui.id_order.setText('')
			ui.id_prod_o.setText('')
			ui.count.setText('')
			ui.price.setText('')
			ui.logs.setText(f'База данных обновлена!\n{logs}')

	def back():
		Ord_Det.close()
		menu()

	ui.id_ord_det.returnPressed.connect(add_od)
	ui.id_order.returnPressed.connect(add_od)
	ui.id_prod_o.returnPressed.connect(add_od)
	ui.count.returnPressed.connect(add_od)
	ui.price.returnPressed.connect(add_od)
	ui.add_od.clicked.connect(add_od)
	ui.del_od.clicked.connect(del_od)
	ui.back_od.clicked.connect(back)

def category():
	global Category
	Category = QtWidgets.QWidget()
	ui = Ui_Category()
	ui.setupUi(Category)
	Menu.close()
	Category.show()
	ui.logs.setReadOnly(True)

	logs = 'ID категории | Наз-ие категории'
	sql.execute('''SELECT * from Categories''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]}'
	ui.logs.setText(f'{logs}')

	def add_cat():
		cat_id = ui.id_cat.text()
		cat_name = ui.name_cat.text()

		if cat_id == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT category_id FROM Categories WHERE category_id = "{cat_id}"')
			if sql.fetchone() is None:
				sql.execute(f'INSERT INTO Categories VALUES(?, ?)', (cat_id, cat_name))
				db.commit()

				logs = 'ID категории | Наз-ие товара'
				sql.execute('''SELECT * from Categories''')
				for i in sql.fetchall():
					logs += f'\n{i[0]} | {i[1]}'

				ui.id_cat.setText('')
				ui.name_cat.setText('')
				ui.logs.setText(f'База данный обновлена!\n{logs}')
			else:
				ui.id_cat.setText('')
				ui.name_cat.setText('')

	def del_cat():
		id_cat = ui.id_cat.text()

		if id_cat == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute('''DELETE FROM Categories WHERE category_id = ?''', (id_cat,))
			db.commit()

			logs = 'ID категории | Наз-ие товара'
			sql.execute('''SELECT * from Categories''')
			for i in sql.fetchall():
				logs += f'\n{i[0]} | {i[1]}'

			ui.id_cat.setText('')
			ui.name_cat.setText('')
			ui.logs.setText(f'База данный обновлена!\n{logs}')

	def back():
		Category.close()
		menu()

	ui.id_cat.returnPressed.connect(add_cat)
	ui.name_cat.returnPressed.connect(add_cat)
	ui.add_cat.clicked.connect(add_cat)
	ui.del_cat.clicked.connect(del_cat)
	ui.back_cat.clicked.connect(back)

def order():
	global Order
	Order = QtWidgets.QWidget()
	ui = Ui_Order()
	ui.setupUi(Order)
	Menu.close()
	Order.show()
	ui.logs.setReadOnly(True)

	logs = 'ID заказа | ID клиента | Дата заказа | Итог. цена'
	sql.execute('''SELECT * from Orders''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]}'
	ui.logs.setText(f'{logs}')

	def add_o():
		id_order = ui.id_order.text()
		id_client_o = ui.id_client_o.text()
		date_order_o = ui.date_order_o.text()
		price_o = ui.price_o.text()

		if id_order == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT order_id FROM Orders WHERE order_id = "{id_order}"')
			if sql.fetchone() is None:
				sql.execute(f'INSERT INTO Orders VALUES(?, ?, ?, ?)', (id_order, id_client_o, date_order_o, price_o))
				db.commit()

				logs = 'ID заказа | ID клиента | Дата заказа | Итог. цена'
				sql.execute('''SELECT * from Orders''')
				for i in sql.fetchall():
					logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]}'

				ui.id_order.setText('')
				ui.id_client_o.setText('')
				ui.date_order_o.setText('')
				ui.price_o.setText('')
				ui.logs.setText(f'База данный обновлена!\n{logs}')
			else:
				ui.id_order.setText('')
				ui.id_client_o.setText('')
				ui.date_order_o.setText('')
				ui.price_o.setText('')

	def del_o():
		id_order = ui.id_order.text()

		if id_order == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute('''DELETE FROM Orders WHERE order_id = ?''', (id_order,))
			db.commit()

			logs = 'ID заказа | ID клиента | Дата заказа | Итог. цена'
			sql.execute('''SELECT * from Orders''')
			for i in sql.fetchall():
				logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]}'

			ui.id_order.setText('')
			ui.id_client_o.setText('')
			ui.date_order_o.setText('')
			ui.price_o.setText('')
			ui.logs.setText(f'База данный обновлена!\n{logs}')

	def back():
		Order.close()
		menu()

	ui.id_order.returnPressed.connect(add_o)
	ui.id_client_o.returnPressed.connect(add_o)
	ui.date_order_o.returnPressed.connect(add_o)
	ui.price_o.returnPressed.connect(add_o)
	ui.add_o.clicked.connect(add_o)
	ui.del_o.clicked.connect(del_o)
	ui.back_o.clicked.connect(back)

def product():
	global Product
	Product = QtWidgets.QWidget()
	ui = Ui_Product()
	ui.setupUi(Product)
	Menu.close()
	Product.show()
	ui.logs.setReadOnly(True)

	logs = 'ID продукта | Наим-ие тов. | Описание товара | Цена за ед. | ID кат.'
	sql.execute('''SELECT * from Products''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'
	ui.logs.setText(f'{logs}')

	def add_prod():
		id_prod = ui.id_prod.text()
		name_prod = ui.name_prod.text()
		cap_prod = ui.cap_prod.text()
		price_prod = ui.price_prod.text()
		id_cat = ui.id_cat.text()

		if id_prod == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT product_id FROM Products WHERE product_id = "{id_prod}"')
			if sql.fetchone() is None:
				sql.execute(f'INSERT INTO Products VALUES(?, ?, ?, ?, ?)', (id_prod, name_prod, cap_prod, price_prod, id_cat))
				db.commit()

				logs = 'ID продукта | Наим-ие тов. | Описание товара | Цена за ед. | ID кат.'
				sql.execute('''SELECT * from Products''')
				for i in sql.fetchall():
					logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

				ui.id_prod.setText('')
				ui.name_prod.setText('')
				ui.cap_prod.setText('')
				ui.price_prod.setText('')
				ui.id_cat.setText('')
				ui.logs.setText(f'База данный обновлена!\n{logs}')
			else:
				ui.id_prod.setText('')
				ui.name_prod.setText('')
				ui.cap_prod.setText('')
				ui.price_prod.setText('')
				ui.id_cat.setText('')

	def del_prod():
		id_prod = ui.id_prod.text()

		if id_prod == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute('''DELETE FROM Products WHERE product_id = ?''', (id_prod,))
			db.commit()

			logs = 'ID продукта | Наим-ие тов. | Описание товара | Цена за ед. | ID кат.'
			sql.execute('''SELECT * from Products''')
			for i in sql.fetchall():
				logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

			ui.id_prod.setText('')
			ui.name_prod.setText('')
			ui.cap_prod.setText('')
			ui.price_prod.setText('')
			ui.id_cat.setText('')
			ui.logs.setText(f'База данный обновлена!\n{logs}')

	def back():
		Product.close()
		menu()

	ui.id_prod.returnPressed.connect(add_prod)
	ui.name_prod.returnPressed.connect(add_prod)
	ui.cap_prod.returnPressed.connect(add_prod)
	ui.price_prod.returnPressed.connect(add_prod)
	ui.id_cat.returnPressed.connect(add_prod)
	ui.add_prod.clicked.connect(add_prod)
	ui.del_prod.clicked.connect(del_prod)
	ui.back_prod.clicked.connect(back)

def mark_res():
	global Mar_Res
	Mar_Res = QtWidgets.QWidget()
	ui = Ui_Mar_Res()
	ui.setupUi(Mar_Res)
	Menu.close()
	Mar_Res.show()
	ui.logs.setReadOnly(True)

	logs = 'ID иссл-ия | Наз-ие иссл-ия | Описание иссл-ия'
	sql.execute('''SELECT * from MarketingResearches''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]}'
	ui.logs.setText(f'{logs}')

	def add_mr():
		id_m = ui.id_m.text()
		name_m = ui.name_m.text()
		cap_m = ui.cap_m.text()

		if id_m == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT research_id FROM MarketingResearches WHERE research_id = "{id_m}"')
			if sql.fetchone() is None:
				sql.execute(f'INSERT INTO MarketingResearches VALUES(?, ?, ?)', (id_m, name_m, cap_m))
				db.commit()

				logs = 'ID иссл-ия | Наз-ие иссл-ия | Описание иссл-ия'
				sql.execute('''SELECT * from MarketingResearches''')
				for i in sql.fetchall():
					logs += f'\n{i[0]} | {i[1]} | {i[2]}'

				ui.id_m.setText('')
				ui.name_m.setText('')
				ui.cap_m.setText('')
				ui.logs.setText(f'База данный обновлена!\n{logs}')
			else:
				ui.id_m.setText('')
				ui.name_m.setText('')
				ui.cap_m.setText('')			

	def del_mr():
		id_m = ui.id_m.text()

		if id_m == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute('''DELETE FROM MarketingResearches WHERE research_id = ?''', (id_m,))
			db.commit()

			logs = 'ID иссл-ия | Наз-ие иссл-ия | Описание иссл-ия'
			sql.execute('''SELECT * from MarketingResearches''')
			for i in sql.fetchall():
				logs += f'\n{i[0]} | {i[1]} | {i[2]}'

			ui.id_m.setText('')
			ui.name_m.setText('')
			ui.cap_m.setText('')
			ui.logs.setText(f'База данный обновлена!\n{logs}')

	def back():
		Mar_Res.close()
		menu()

	ui.id_m.returnPressed.connect(add_mr)
	ui.name_m.returnPressed.connect(add_mr)
	ui.cap_m.returnPressed.connect(add_mr)
	ui.add_m.clicked.connect(add_mr)
	ui.del_m.clicked.connect(del_mr)
	ui.back_m.clicked.connect(back)

def clients():
	global Clients
	Clients = QtWidgets.QWidget()
	ui = Ui_Clients()
	ui.setupUi(Clients)
	Menu.close()
	Clients.show()
	ui.logs.setReadOnly(True)

	logs = 'ID клиента | Имя | Фамилия | Email | Номер телефона'
	sql.execute('''SELECT * from Customers''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'
	ui.logs.setText(f'{logs}')

	def add_cl():
		id_cl = ui.id_cl.text()
		name_cl = ui.name_cl.text()
		fam_cl = ui.fam_cl.text()
		mail_cl = ui.mail_cl.text()
		num_cl = ui.num_cl.text()

		if id_cl == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT customer_id FROM Customers WHERE customer_id = "{id_cl}"')
			if sql.fetchone() is None:
				sql.execute(f'INSERT INTO Customers VALUES(?, ?, ?, ?, ?)', (id_cl, name_cl, fam_cl, mail_cl, num_cl))
				db.commit()

				logs = 'ID клиента | Имя | Фамилия | Email | Номер телефона'
				sql.execute('''SELECT * from Customers''')
				for i in sql.fetchall():
					logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

				ui.id_cl.setText('')
				ui.name_cl.setText('')
				ui.fam_cl.setText('')
				ui.mail_cl.setText('')
				ui.num_cl.setText('')
				ui.logs.setText(f'База данный обновлена!\n{logs}')
			else:
				ui.id_cl.setText('')
				ui.name_cl.setText('')
				ui.fam_cl.setText('')
				ui.mail_cl.setText('')
				ui.num_cl.setText('')

	def del_cl():
		id_cl = ui.id_cl.text()

		if id_cl == '':
			ui.logs.setText('Ошибка')
		else:
			sql.execute('''DELETE FROM Customers WHERE customer_id = ?''', (id_cl,))
			db.commit()

			logs = 'ID клиента | Имя | Фамилия | Email | Номер телефона'
			sql.execute('''SELECT * from Customers''')
			for i in sql.fetchall():
				logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

			ui.id_cl.setText('')
			ui.name_cl.setText('')
			ui.fam_cl.setText('')
			ui.mail_cl.setText('')
			ui.num_cl.setText('')
			ui.logs.setText(f'База данный обновлена!\n{logs}')

	def back():
		Clients.close()
		menu()


	ui.id_cl.returnPressed.connect(add_cl)
	ui.name_cl.returnPressed.connect(add_cl)
	ui.fam_cl.returnPressed.connect(add_cl)
	ui.mail_cl.returnPressed.connect(add_cl)
	ui.num_cl.returnPressed.connect(add_cl)
	ui.add_cl.clicked.connect(add_cl)
	ui.del_cl.clicked.connect(del_cl)
	ui.back_cl.clicked.connect(back)

def exit():
	sys.exit(app.exec_())


def menu():
	global Menu
	Menu = QtWidgets.QWidget()
	ui = Ui_Menu()
	ui.setupUi(Menu)
	Menu.show()

	ui.order_details.clicked.connect(ord_det)
	ui.category.clicked.connect(category)
	ui.order.clicked.connect(order)
	ui.product.clicked.connect(product)
	ui.mark_res.clicked.connect(mark_res)
	ui.clients.clicked.connect(clients)
	ui.exit.clicked.connect(exit)

ui.email.returnPressed.connect(check)
ui.pass_email.returnPressed.connect(check)
ui.enter.clicked.connect(check)

ui.reg_avt.clicked.connect(reg)

sys.exit(app.exec_())