from model import *
from connection import *
from view import *
from statistics import *
from logger import *
from parser import *

class Controller():

    def __init__(self):
        self.logger = RoleLogger()
        self.logger.basicConfig("logfile.txt")

    def authorizate(self, login, password):
        base = JsonParser().get_base()
        data = JsonParser().get_connection_data()
        users_data = [i for i in data]
        for i in users_data:
            for k, v in i.items():
                if k == 'start_user':
                    start_user = v
        #start_user = users_data[0].get('start_user')
        self.auth_data = AuthData(base, str(start_user.get('dbname')),
                                        str(start_user.get('user')),
                                        str(start_user.get('password')),
                                        str(start_user.get('host')),
                                        str(start_user.get('port')))
        self.user = StartUser(self.auth_data.user)
        try:
            PostgresqlConnector().connect(self.auth_data)
        except:
            self.logger.error("Не удалось подключиться под ролью читателя.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return "Не удалось подключиться под ролью читателя."
        user = Authorizator().auhorizate(login, password)
        if (user):
            # find id
            manid = EmployeeSelector().find_id_role(user)
            app_user = User(login, password, user.role, manid, user.name)
        else:
            self.logger.error("Пользователь с введенными данными не существует.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            PostgresqlConnector().disconnect()
            return "Пользователь с введенными данными не существует."
        try:
            PostgresqlConnector().disconnect()
            employee = None
            for i in users_data:
                for k, v in i.items():
                    if k == app_user.role:
                        employee = v
            if not employee:
                self.logger.error("Данные файла конфигурации повреждены.",
                                  inspect.getframeinfo(inspect.currentframe()).function,
                                  self.user)
                return "Данные файла конфигурации повреждены."

            self.auth_data = AuthData(base, str(employee.get('dbname')),
                                      str(employee.get('user')),
                                      str(employee.get('password')),
                                      str(employee.get('host')),
                                      str(employee.get('port')))
            PostgresqlConnector().connect(self.auth_data)
            self.user = app_user
            self.logger.info("Успешное подключение под ролью сотрудника.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return
        except:
            self.logger.error("Не удалось подключиться под ролью сотрудника!",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return "Не удалось подключиться под ролью сотрудника!"

    def disconnect(self):
        PostgresqlConnector().disconnect()

    def insert_company(self, company):
        result = CompanyInserter().insert(company, self.user)
        if (result):
            self.logger.info("Успешное добавление компании.",
                             inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return
        self.logger.error("Ошибка при добавлении компании.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def insert_deal(self, deal, company):
        result = DealInserter().insert(deal, company)
        if (type(result) == bool):
            self.logger.info("Успешное добавление сделки.",
                             inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return result
        self.logger.error("Ошибка при добавлении сделки.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def find_region_plans_manager(self):
        manager_id = self.user.id
        region = RegionSelector().find_by_manager_id(manager_id)
        result = ManagerSelector().find_plans(region)
        if (result):
            return result
        self.logger.error("Ошибка при поиске планов менеджеров в регионе.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def find_region_plans_admin(self):
        admin_id = self.user.id
        region = RegionSelector().find_by_admin_id(admin_id)
        result = AdministratorSelector().find_plans(region)
        if (result):
            return result
        self.logger.error("Ошибка при поиске планов администраторов в регионе.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def find_region_plans_director(self):
        director_id = self.user.id
        region = RegionSelector().find_by_director_id(director_id)
        result = DirectorSelector().find_plans(region)
        if (result):
            return result
        self.logger.error("Ошибка при поиске планов администраторов в регионе.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def find_director_deals_approve(self):
        director_id = self.user.id
        region = RegionSelector().find_by_director_id(director_id)
        result = DirectorSelector().find_deals_approve(region)
        if (result):
            return result
        self.logger.error("Ошибка при поиске процента одобрения компаний.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def find_manager_deals(self):
        result = ManagerSelector().find_deals(self.user.id)
        if (result):
            return result
        self.logger.error("Ошибка при поиске сделок менеджера.",
                          inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return "Some error"

    def get_info(self, table):
        if (table == "Companies"):
            result = CompanySelector().find_all()
            if result:
                return result
            return "Таблица компаний пуста."
        elif (table == "Managers"):
            result = ManagerSelector().find_all()
            if result:
                return result
            return "Таблица менеджеров пуста."
        elif (table == "Deals"):
            result = DealSelector().find_all()
            if result:
                return result
            return "Таблица сделок пуста."
        elif (table == "Employers"):
            result = EmployeeSelector().find_all()
            if result:
                return result
            return "Таблица сотрудников пуста."
        elif (table == "Directors"):
            result = DirectorSelector().find_all()
            if result:
                return result
            return "Таблица директоров пуста."
        elif (table == "Administrators"):
            result = AdministratorSelector().find_all()
            if result:
                return result
            return "Таблица администраторов пуста."
        elif (table == "Regions"):
            result = RegionSelector().find_all()
            if result:
                return result
            return "Таблица регионов пуста."
        elif (table == "Districts"):
            result = DistrictSelector().find_all()
            if result:
                return result
            return "Таблица округов пуста."
        else:
            self.logger.warning("Неверные данные.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)

    def plot_manager_plan(self, view):
        result = self.find_region_plans_manager()
        if type(result) == str:
            self.logger.error("Ошибка при построении графика.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return "Bad"
        PlotCanvas().plot_plan(view.mywidget, result)
        self.logger.info("График успешно построен.",
                         inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return result

    def plot_admin_plan(self, view):
        result = self.find_region_plans_admin()
        if type(result) == str:
            self.logger.error("Ошибка при построении графика.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return result
        PlotCanvas().plot_plan(view.mywidgett, result)
        self.logger.info("График успешно построен.",
                         inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return

    def plot_director_plan(self, view):
        result = self.find_region_plans_director()
        if type(result) == str:
            self.logger.error("Ошибка при построении графика.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return result
        PlotCanvas().plot_plan(view.mywidgettt, result)
        self.logger.info("График успешно построен.",
                         inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return

    def plot_manager_deals(self, view):
        result = self.find_manager_deals()
        if type(result) == str:
            self.logger.error("Ошибка при построении графика.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return result
        PlotCanvas().plot_manager_deals(view.mywidget, result)
        self.logger.info("График успешно построен.",
                         inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return

    def plot_deals_approve(self, view):
        result = self.find_director_deals_approve()
        if type(result) == str:
            self.logger.error("Ошибка при построении графика.",
                              inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
            return result
        PlotCanvas().plot_deals_approve(view.mywidgettt, result)
        self.logger.info("График успешно построен.",
                         inspect.getframeinfo(inspect.currentframe()).function,
                              self.user)
        return

