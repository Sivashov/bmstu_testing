
class User():
    def __init__(self, login, password, role, id, name):
        self.login = login
        self.password = password
        self.role = role
        self.id = id
        self.name = name

class StartUser():
    def __init__(self, role, name="start_user"):
        self.role = role
        self.name = name


class AuthData():
    def __init__(self, db, dbname, user, password, host, port):
        self.db = db
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def set_db(self, proxy):
        self.database_proxy = proxy



class Employee():
    def __init__(self, id, name, age, month_plan, role, login, password):
        self.id = id
        self.name = name
        self.age = age
        self.month_plan = month_plan
        self.role = role
        self.login = login
        self.password = password

class Manager(Employee):
    def __init__(self, id, name, age, month_plan, district_id, employee_id):
        self.id = id
        self.name = name
        self.age = age
        self.month_plan = month_plan
        self.district_id = district_id
        self.employee_id = employee_id

class Director(Employee):
    def __init__(self, id, name, age, month_plan, region_id, employee_id):
        self.id = id
        self.name = name
        self.age = age
        self.month_plan = month_plan
        self.region_id = region_id
        self.employee_id = employee_id

class Administrator(Employee):
    def __init__(self, id, name, age, month_plan, director_id, district_id, employee_id):
        self.id = id
        self.name = name
        self.age = age
        self.month_plan = month_plan
        self.director_id = director_id
        self.district_id = district_id
        self.employee_id = employee_id

class Company():
    def __init__(self, name, has_online, has_offline):
        self.name = name
        self.has_online = has_online
        self.has_offline = has_offline

class OutputCompany(Company):
    def __init__(self, id, name, has_online, has_offline):
        self.id = id
        self.name = name
        self.has_online = has_online
        self.has_offline = has_offline

class Region():
    def __init__(self, id, name, director_id, population, number_of_companies):
        self.id = id
        self.name = name
        self.director_id = director_id
        self.population = population
        self.number_of_companies = number_of_companies

class District():
    def __init__(self, id, name, region_id, administrator_id, population, number_of_companies):
        self.id = id
        self.name = name
        self.region_id = region_id
        self.administrator_id = administrator_id
        self.population = population
        self.number_of_companies = number_of_companies

class AddCompany(Company):
    def __init__(self, name, region_id, manager_id, has_online, has_offline):
        self.name = name
        self.region_id = region_id
        self.manager_id = manager_id
        self.has_online = has_online
        self.has_offline = has_offline

class Deal():
    def __init__(self, id, orderer_name, deal_sum, deal_type, is_approved, deal_time):
        self.id = id
        self.orderer_name = orderer_name
        self.deal_sum = deal_sum
        self.deal_type = deal_type
        self.is_approved = is_approved
        self.deal_time = deal_time

class InpDeal(Deal):
    def __init__(self, orderer_name, deal_sum, deal_type):
        self.orderer_name = orderer_name
        self.deal_sum = deal_sum
        self.deal_type = deal_type

class InsertDeal(Deal):
    def __init__(self, orderer_name, deal_sum, deal_type, is_approved, deal_time):
        self.orderer_name = orderer_name
        self.deal_sum = deal_sum
        self.deal_type = deal_type
        self.is_approved = is_approved
        self.deal_time = deal_time



class CmpDealsSum():
    def __init__(self, id, company, sum):
        self.id = id
        self.company = company
        self.deal_sum = sum

class EmployersPlans():
    def __init__(self, id, name, plan):
        self.id = id
        self.name = name
        self.plan = plan

class EmployeePlanAchieve():
    def __init__(self, name, plan_prcntg):
        self.name = name
        self.plan_prcntg = plan_prcntg

class CmpApprove():
    def __init__(self, name, approve_prcntg):
        self.name = name
        self.approve_prcntg = approve_prcntg

class CmpDealsCount():
    def __init__(self, id, name, count):
        self.id = id
        self.name = name
        self.count = count