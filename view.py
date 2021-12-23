from entities import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QButtonGroup
from controller import *
from PyQt5 import uic
from auth_ui import AuthUi
from manager_ui import ManagerUi
from administrator_ui import AdministratorUi
from director_ui import DirectorUi
import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)

        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)



class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        '''self.ui = Ui_MainWindow()
        self.ui.setupUi(self)'''

        uic.loadUi('EmployeeApp.ui', self)
        self.setWindowTitle("Authorization")

        self.first = AuthUi()
        self.stackedWidget.addWidget(self.first)
        self.first.signInBtn.clicked.connect(self.check_auth_input)
        self.base_lineedit = [self.first.loginLine, self.first.passwordLine]

        self.second = ManagerUi()
        self.stackedWidget.addWidget(self.second)
        self.second.addCompanyBtn.clicked.connect(self.check_add_company_input)
        self.second.tablesComboBox.addItems(["Companies", "Employers", "Deals", "Managers",
                                             "Regions", "Districts", "Administrators",
                                             "Directors"])
        self.second.tablesComboBox.activated[str].connect(self.check_info_input)
        self.second.managerStatBox.addItems(["Сделки компаний", "Выполнение плана"])
        self.second.managerStatBox.activated[str].connect(self.plot_manager)
        self.second.exitBtn.clicked.connect(self.go_to_auth)

        self.third = AdministratorUi()
        self.stackedWidget.addWidget(self.third)
        self.third.addDealBtn.clicked.connect(self.check_add_deal_input)
        self.third.button_group = QButtonGroup()
        self.third.button_group.addButton(self.third.onlineTypeBtn)
        self.third.button_group.addButton(self.third.offlineTypeBtn)
        self.third.adminStatBox.addItems(["Выполнение плана"])
        self.third.adminStatBox.activated[str].connect(self.plot_admin)
        self.third.tablesComboBox.addItems(["Companies", "Employers", "Deals", "Managers",
                                             "Regions", "Districts", "Administrators",
                                             "Directors"])
        self.third.tablesComboBox.activated[str].connect(self.check_info_input)
        self.third.exitBtn.clicked.connect(self.go_to_auth)


        self.fourth = DirectorUi()
        self.stackedWidget.addWidget(self.fourth)
        self.fourth.tablesComboBox.addItems(["Companies", "Employers", "Deals", "Managers",
                                             "Regions", "Districts", "Administrators",
                                             "Directors"])
        self.fourth.tablesComboBox.activated[str].connect(self.check_info_input)
        self.fourth.directorStatBox.addItems(["Выполнение плана", "Одобрение сделок"])
        self.fourth.directorStatBox.activated[str].connect(self.plot_director)
        self.fourth.exitBtn.clicked.connect(self.go_to_auth)

        self.init_widget()
        #self.check_info_input("Companies")


    def set_controller(self, controller):
        self.controller = controller

    def fill_companies_third(self):
        result = self.controller.get_info("Companies")
        items = []
        for company in result:
            items.append(company.name)
        self.third.companyBox.addItems(items)

    def init_widget(self):
        self.mywidget = MyWidget()
        self.layoutvertical = QVBoxLayout(self.second.statGraph)
        self.layoutvertical.addWidget(self.mywidget)
        self.mywidgett = MyWidget()
        self.layoutvertical = QVBoxLayout(self.third.statGraph)
        self.layoutvertical.addWidget(self.mywidgett)
        self.mywidgettt = MyWidget()
        self.layoutvertical = QVBoxLayout(self.fourth.statGraph)
        self.layoutvertical.addWidget(self.mywidgettt)

    def plot_manager(self, text):
        if text == "Сделки компаний":
            result = self.controller.plot_manager_deals(self)
        elif text == "Выполнение плана":
            result = self.controller.plot_manager_plan(self)
        if result:
            self.error_handler(result)
            return 1
        return 0

    def plot_admin(self, text):
        if text == "Выполнение плана":
            result = self.controller.plot_admin_plan(self)
        if result:
            self.error_handler(result)
        return

    def plot_director(self, text):
        if text == "Одобрение сделок":
            result = self.controller.plot_deals_approve(self)
        elif text == "Выполнение плана":
            result = self.controller.plot_director_plan(self)
        if result:
            self.error_handler(result)
        return

    def go_to_auth(self):
        self.stackedWidget.setCurrentIndex(0)


    def go_to_manager(self):
        self.stackedWidget.setCurrentIndex(1)
        self.resize(1000, 1000)
        self.stackedWidget.resize(1000, 1000)
        self.second.resize(1000, 1000)

    def go_to_administrator(self):
        self.stackedWidget.setCurrentIndex(2)
        self.resize(1000, 1000)
        self.stackedWidget.resize(1000, 1000)
        self.third.resize(1000, 1000)
        self.fill_companies_third()

    def go_to_director(self):
        self.stackedWidget.setCurrentIndex(3)
        #self.setGeometry(100, 100, 1800, 600)
        #self.setGeometry(100, 100, 1800, 600)
        #self.fourth.resize(1400, 600)
        #self.stackedWidget.resize(1400, 1000)

    def check_auth_input(self):
        for line_edit in self.base_lineedit:
            if len(line_edit.text()) == 0:
                self.error_handler("Поле пусто.")
                return
        error = self.controller.authorizate(self.base_lineedit[0].text(), self.base_lineedit[1].text())
        if (error):
            self.error_handler(error)
            return
        self.welcome(self.controller.user.name)
        if self.controller.user.role == "manager":
            self.go_to_manager()
        elif self.controller.user.role == "administrator":
            self.go_to_administrator()
        elif self.controller.user.role == "director":
            self.go_to_director()
        self.setWindowTitle("BankApp")
        self.stackedWidget.resize(1200, 800)
        self.second.resize(800, 600)
        self.resize(800, 600)

    def check_add_company_input(self):
        # getting data from fields
        name = self.second.companyName.text()
        if len(name) == 0:
            self.error_handler("Поле пусто.")
            return
        has_online = True if self.second.hasOnlineBox.isChecked() else False
        has_offline = True if self.second.hasOfflineBox.isChecked() else False
        company = Company(name,
                          has_online,
                          has_offline)
        error = self.controller.insert_company(company)
        if (error):
            self.error_handler(error)
        self.show_info("Компания успешно добавлена!")
        return

    def check_add_deal_input(self):
        # getting data from fields
        name = self.third.ordererName.text()
        if len(name) == 0:
            self.error_handler("Поле пусто.")
            return
        sum = self.third.dealSumLine.text()
        if len(sum) == 0:
            self.error_handler("Поле пусто.")
            return
        try:
            sum = int(sum)
        except:
            return "Некорректная сумма."
        if self.third.onlineTypeBtn.isChecked():
            kind = "online"
        elif self.third.offlineTypeBtn.isChecked():
            kind = "offline"
        deal = InpDeal(name,
                       int(sum),
                       kind)

        company = self.third.companyBox.currentText()
        cmp = CompaniesStore().get_by_name(company)
        flag = 0
        if (kind == "online" and cmp.has_online):
            flag = 1
        if (kind == "offline" and cmp.has_offline):
            flag = 1
        if (flag == 0):
            self.error_handler("Компания не допускает сделки данного типа!")
            return
        error = self.controller.insert_deal(deal, company)
        if (type(error) == str):
            self.error_handler(error)
            return
        if error == True:
            self.show_info("Сделка успешно добавлена!\nСтатус: одобрена.")
        else:
            self.show_info("Сделка успешно добавлена!\nСтатус: не одобрена.")
        return

    def check_info_input(self, text):
        res = self.controller.get_info(text)
        if (type(res) == str):
            self.error_handler(res)
            return
        fields_count = len(res[0].__dict__)
        res_len = len(res)
        if (self.controller.user.role == "manager"):
            tabwidget = self.second
        elif (self.controller.user.role == "administrator"):
            tabwidget = self.third
        elif (self.controller.user.role == "director"):
            tabwidget = self.fourth

        tabwidget.infoOutputTable.setRowCount(res_len)
        tabwidget.infoOutputTable.setColumnCount(fields_count)
        tabwidget.infoOutputTable.setHorizontalHeaderLabels([key for key in res[0].__dict__])
        for i in range(res_len):
            line = res[i].__dict__
            items = line.keys()
            k = 0
            for item in items:
                tabwidget.infoOutputTable.setItem(i, k, QTableWidgetItem(str(line[item])))
                k += 1

    def error_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def show_info(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def welcome(self, name):
        opts = {"hey": ('Доброе утро, ', 'Добрый день, ', 'Добрый вечер, ', 'Доброй ночи, ')}

        now = datetime.datetime.now()
        print(now.hour)
        if now.hour > 4 and now.hour <= 12:
            greet = opts["hey"][0]
        if now.hour > 12 and now.hour <= 16:
            greet = opts["hey"][1]
        if now.hour > 16 and now.hour <= 24:
            greet = opts["hey"][2]
        if now.hour >= 0 and now.hour <= 4:
            greet = opts["hey"][3]

        msg = greet + str(name) + "!\nДа прибудет с тобой сила."
        QtWidgets.QMessageBox.about(self, 'Приветствие', msg)

class BaseView():
    pass

class ConsoleView(BaseView):

    def __init__(self, controller):
        self.controller = controller

    def set_controller(self, controller):
        self.controller = controller

    def auth_menu(self):
        self.show_auth_menu()
        login = self.input("Login:", "str")
        password = self.input("Password:", "str")
        error = self.controller.authorizate(login, password)
        if (error):
            self.show_error(error)
            return
        self.welcome(self.controller.user.name)
        if self.controller.user.role == "manager":
            self.manager_menu()
        elif self.controller.user.role == "administrator":
            pass
        elif self.controller.user.role == "director":
            pass
        else:
            print("Неверный ввод.")
        return

    def manager_menu(self):
        choice = -1
        while (choice != 0):
            self.show_manager_menu()
            choice = self.input("", "int")
            if (choice == 1):
                sel_choice = -1
                while (sel_choice != 0):
                    self.show_manager_find_menu()
                    sel_choice = self.input("", "int")
                    if (sel_choice == 1):
                        result = self.controller.get_info("Companies")
                        self.show_res_companies(result)
                    elif (sel_choice == 2):
                        result = self.controller.get_info("Managers")
                        self.show_res_managers(result)
                    elif sel_choice == 0:
                        pass
                    else:
                        self.wrong_choice()
            elif (choice == 2):
                self.show_manager_statistics("Сделки компаний")
            elif choice == 3:
                company = self.add_company()  # get data of company from console
                error = self.controller.insert_company(company)
                if (error):
                    self.show_error(error)
                    return 0
                self.info("Компания успешно добавлена.")
            elif choice == 0:
                pass
            else:
                self.wrong_choice()
                return -1
        return 1

    def welcome(self, name):
        opts = {"hey": ('Доброе утро, ', 'Добрый день, ', 'Добрый вечер, ', 'Доброй ночи, ')}

        now = datetime.datetime.now()
        print(now.hour)
        if now.hour > 4 and now.hour <= 12:
            greet = opts["hey"][0]
        if now.hour > 12 and now.hour <= 16:
            greet = opts["hey"][1]
        if now.hour > 16 and now.hour <= 24:
            greet = opts["hey"][2]
        if now.hour >= 0 and now.hour <= 4:
            greet = opts["hey"][3]

        msg = greet + str(name) + "!\nДа прибудет с тобой сила."
        print(msg)

    def input(self, message, type):
        if (type == "int"):
            res = int(input(message))
            return res
        elif (type == "str"):
            res = str(input(message))
            return res

    def info(self, msg):
        print(msg)

    def wrong_choice(self):
        print("Incorrect choice! Try again.\n")

    def show_manager_menu(self):
        print("\nЧто вы хотите сделать?".center(25))
        print("1. Вывести данные таблицы.")
        print("2. Получить статистику.")
        print("3. Добавить компанию.")
        print("0. Выход.\n")

    def show_auth_menu(self):
        print("\nВведите данные для входа:\n")

    def show_manager_find_menu(self):
        print("\nВыберите таблицу:")
        print("1. Компании.")
        print("2. Менеджеры.")
        print("0. Exit.\n")

    def show_manager_statistics(self, text):
        if text == "Сделки компаний":
            result = self.controller.plot_manager_deals(self)
        elif text == "Выполнение плана":
            result = self.controller.plot_manager_plan(self)
        if result:
            self.error_handler(result)
            return 1
        return 0

    def add_company(self):
        try:
            name = str(input("Название: "))
            has_online = str(input("Online (да или нет): "))
            has_offline = str(input("Offline (да или нет): "))
            company = Company(name,
                              True if has_online == "да" else False,
                              True if has_offline == "да" else False)
            return company
        except:
            raise ValueError


    def show_res_managers(self, managers):
        print("{:^10s}┃{:^20s}┃{:^10s}┃{:^10s}┃{:^10s}┃{:^10s}".format("id", "name", "age", "month plan", "district id",
                                                                       "employee id"))
        print("━"*75)
        for i in managers:
            print("{:^10d}┃{:^20s}┃{:^10d}┃{:^10d}┃{:^10d}┃{:^10d}".format(i.id,
                                                                           i.name,
                                                                           i.age,
                                                                           i.month_plan,
                                                                           i.district_id,
                                                                           i.employee_id))
    def show_res_companies(self, companies):
        print("{:^10s}┃{:^20s}┃{:^10s}┃{:^10s}".format("id", "name", "online", "offline"))
        print("━" * 51)
        for i in companies:
            print("{:^10d}┃{:^20s}┃{:^10s}┃{:^10s}".format(i.id,
                                                           i.name,
                                                           "yes" if i.has_online else "no",
                                                           "yes" if i.has_offline else "no"))

    def show_error(self, message):
        print(message)