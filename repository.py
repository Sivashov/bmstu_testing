from models import *
from entities import *
import calendar
import datetime

class StoreException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors

class BaseStore():
    def get_all(self):
        pass

    def get_all_param(self, params):
        pass

    def get_by_id(self, id):
        pass

    def get_by_name(self, name):
        pass

class RegionsStore(BaseStore):
    def get_all(self):
        try:
            result = Regions.select()
            regions = []
            for reg in result:
                regions.append(Region(reg.id,
                                      reg.name,
                                      reg.director_id,
                                      reg.population,
                                      reg.number_of_companies))
            return regions
        except Exception as e:
            #raise StoreException('error selecting regions')
            return 0

    def get_all_param(self, params):
        try:
            result = Regions.select().where(params)
            return result
        except Exception as e:
            #raise StoreException('error selecting regions')
            return 0

class DistrictsStore(BaseStore):
    def get_all(self):
        try:
            result = Districts.select()
            districts = []
            for dis in result:
                districts.append(District(dis.id,
                                          dis.name,
                                          dis.region_id.id,
                                          dis.administrator_id,
                                          dis.population,
                                          dis.number_of_companies))
            return districts
        except Exception as e:
            raise StoreException('error selecting districts')

    def get_by_name(self, name):
        try:
            result = Districts.select() \
                .where(Districts.name.contains(name))
            dists = []
            for dis in result:
                dists.append(District(dis.id,
                                          dis.name,
                                          dis.region_id.id,
                                          dis.administrator_id,
                                          dis.population,
                                          dis.number_of_companies))
            return dists
        except Exception as e:
            raise StoreException('error selecting managers')

class EmployersStore(BaseStore):
    def get_all(self):
        try:
            result = Employers.select()
            employers = []
            for emp in result:
                employers.append(Employee(emp.id,
                                          emp.name,
                                          emp.age,
                                          emp.month_plan,
                                          emp.role,
                                          emp.login,
                                          emp.password))
            return employers
        except Exception as e:
            raise StoreException('error selecting employers')

    def get_all_param(self, params):
        try:
            result = Employers.select().where(params)
            return result
        except Exception as e:
            raise StoreException('error selecting employers')

    def get_by_id(self, id):
        try:
            result = Employers.select().where(int(id) == id).get()
            return result
        except Exception as e:
            raise StoreException('error selecting employers')

    def get_by_name(self, name):
        try:
            result = Employers.select().where(Employers.name.contains(name))
            return result
        except Exception as e:
            raise StoreException('error selecting employers')

    def get_manager_id(self, user):
        try:
            query = (Employers.select(Managers.id.alias('id'))
                               .where(Employers.id == int(user.id))
                               .join(Managers, on=(Managers.employee_id == Employers.id)))
            result = []
            for row in query.dicts():
                result.append(row['id'])
            return result[0]
        except Exception as e:
            raise StoreException('error selecting manager id')

    def get_administrator_id(self, user):
        try:
            query = (Employers.select(Administrators.id.alias('id'))
                               .where(Employers.id == int(user.id))
                               .join(Administrators, on=(Administrators.employee_id == Employers.id)))
            result = []
            for row in query.dicts():
                result.append(row['id'])
            return result[0]
        except Exception as e:
            raise StoreException('error selecting administrator id')

    def get_director_id(self, user):
        try:
            query = (Employers.select(Directors.id.alias('id'))
                               .where(Employers.id == int(user.id))
                               .join(Directors, on=(Directors.employee_id == Employers.id)))
            result = []
            for row in query.dicts():
                result.append(row['id'])
            return result[0]
        except Exception as e:
            raise StoreException('error selecting director id')

class ManagersStore(BaseStore):
    def get_all(self):
        try:
            result = Managers.select()\
                            .join(Employers)
            managers = []
            for man in result:
                managers.append(Manager(man.id,
                                        man.employee_id.name,
                                        man.employee_id.age,
                                        man.employee_id.month_plan,
                                        man.district_id.id,
                                        man.employee_id.id))
            return managers
        except Exception as e:
            raise StoreException('error selecting managers')

    def get_all_param(self, params):
        try:
            result = Managers.select()\
                            .join(Employers)\
                            .where(params)
            managers = []
            for man in result:
                managers.append(Manager(man.id,
                                        man.employee_id.name,
                                        man.employee_id.age,
                                        man.employee_id.month_plan,
                                        man.district_id.id))
            return managers
        except Exception as e:
            raise StoreException('error selecting managers')

    def get_by_id(self, id):
        try:
            result = Managers.select().where(int(id) == id).get()
            return result
        except Exception as e:
            raise StoreException('error selecting managers')

    def get_by_name(self, name):
        try:
            result = Managers.select() \
                .join(Employers) \
                .where(Employers.name.contains(name))
            managers = []
            for man in result:
                managers.append(Manager(man.id,
                                        man.employee_id.name,
                                        man.employee_id.age,
                                        man.employee_id.month_plan,
                                        man.district_id.id,
                                        man.employee_id.id))
            return managers
        except Exception as e:
            raise StoreException('error selecting managers')

    def get_region_by_id(self, id):
        try:
            query = (Employers.select(Regions.id.alias('id'), Regions.name.alias('name'),
                                       Regions.director_id.alias('director_id'),
                                       Regions.population.alias('population'),
                                       Regions.number_of_companies.alias('cmpn'))
                               .join(Managers)
                               .join(Districts)
                               .join(Regions)
                               .where(Managers.id == id))
            result = []
            for row in query.dicts():
                result.append(Region(row['id'], row['name'], row['director_id'], row['population'], row['cmpn']))
            return result[0]
        except Exception as e:
            raise StoreException('error selecting region_id')

    def get_deals(self, id):
        try:
            query = (Managers.select(Managers.id.alias('id'), Companies.name.alias('company'),
                                     fn.SUM(Deals.deal_sum).alias('dealsum'))
                              .join(Companies)
                              .join(CompanyDeal)
                              .join(Deals)
                              .where(Managers.id == id, Deals.is_approved)
                              #.where(Managers.id == id, fn.date_part('month', Deals.deal_time) == datetime.date.today().month)
                              .group_by(Companies.name, Managers.id)
                              .order_by(fn.SUM(Deals.deal_sum)))
            result = []
            for row in query.dicts():
                result.append(CmpDealsSum(row['id'], row['company'], row['dealsum']))
            return result
        except Exception as e:
            raise StoreException('error selecting manager deals')

    def get_plans(self, region):
        try:
            query = (Employers.select(Managers.id.alias('id'), Employers.name.alias('name'),
                                      Employers.month_plan.alias('plan'))
                                .join(Managers)
                                .join(Districts)
                                .join(Regions)
                                .where(Regions.id == region.id))
            result = []
            for row in query.dicts():
                result.append(EmployersPlans(row['id'], row['name'], row['plan']))
            return result
        except Exception as e:
            raise StoreException('error selecting managers plans')

class CompaniesStore(BaseStore):
    def get_all(self):
        try:
            result = Companies.select().order_by(Companies.name)
            companies = []
            for com in result:
                companies.append(OutputCompany(com.id,
                                         com.name,
                                         com.has_online,
                                         com.has_offline))
            return companies
        except Exception as e:
            raise StoreException('error selecting companies')

    def get_by_name(self, name):
        try:
            query = Companies.select().where(Companies.name == name)
            res = []
            for com in query:
                res.append(OutputCompany(com.id,
                                        com.name,
                                        com.has_online,
                                        com.has_offline))
            return res[0]
        except Exception as e:
            raise StoreException('error selecting companies')

    def get_all_param(self, params):
        try:
            result = Companies.select().where(params)
            companies = []
            for com in result:
                companies.append(OutputCompany(com.id,
                                         com.name,
                                         com.has_online,
                                         com.has_offline))
            return companies
        except Exception as e:
            raise StoreException('error selecting companies')

    def insert(self, company):
        try:
            count = len(Companies.select())
            print(count)
            result =(Companies.insert(
                    id= count + 1,
                    name= company.name,
                    region_id= company.region_id,
                    manager_id= company.manager_id,
                    has_online= company.has_online,
                    has_offline= company.has_offline)
                     ).execute()
            print(result)
            return result
        except Exception as e:
            raise StoreException('error adding company')

    def delete(self, name):
        try:
            result = Companies.delete().where(Companies.name.contains(name))
            return 1
        except:
            return 0

class DealsStore(BaseStore):
    def get_all(self):
        try:
            result = Deals.select()
            deals = []
            for deal in result:
                deals.append(Deal(deal.id,
                                deal.orderer_name,
                                deal.deal_sum,
                                deal.deal_type,
                                deal.is_approved,
                                deal.deal_time))
            return deals
        except Exception as e:
            #raise StoreException('error selecting deals')
            return 0

    def get_all_param(self, params):
        try:
            result = Deals.select().where(params)
            return result
        except Exception as e:
            raise StoreException('error selecting deals')

    def get_deals_by_region(self, region):
        try:
            query = (Deals.select(Companies.id.alias('id'), Companies.name.alias('name'),
                                  fn.COUNT(Deals.id).alias('cnt'))
                               .join(CompanyDeal)
                               .join(Companies)
                               .join(Regions)
                               .where(Regions.id == region.id) #fn.date_part('month', Deals.deal_time) == 4)
                                #.where(Regions.id == id, fn.date_part('month', Deals.deal_time) == datetime.date.today().month)
                               .group_by(Companies.id, Companies.name)
                               .order_by(fn.COUNT(Deals.id)))
            result = []
            for row in query.dicts():
                result.append(CmpDealsCount(row['id'], row['name'], row['cnt']))
            return result
        except Exception as e:
            raise StoreException('error selecting region_id')

    def get_approved_deals_by_region(self, region):
        try:
            query = (Deals.select(Companies.id.alias('id'), Companies.name.alias('name'),
                                  fn.COUNT(Deals.id).alias('cnt'))
                               .join(CompanyDeal)
                               .join(Companies)
                               .join(Regions)
                               .where(Regions.id == region.id, #fn.date_part('month', Deals.deal_time) == 4,
                                      Deals.is_approved)
                                #.where(Regions.id == id, fn.date_part('month', Deals.deal_time) == datetime.date.today().month)
                               .group_by(Companies.id, Companies.name)
                               .order_by(fn.COUNT(Deals.id)))
            result = []
            for row in query.dicts():
                result.append(CmpDealsCount(row['id'], row['name'], row['cnt']))
            return result
        except Exception as e:
            raise StoreException('error selecting region_id')

    def insert(self, deal):
        try:
            count = len(Deals.select())
            result = (Deals.insert(
                     id= count + 1,
                     orderer_name= deal.orderer_name,
                     deal_sum= deal.deal_sum,
                     deal_type= deal.deal_type,
                     is_approved= deal.is_approved,
                     deal_time= deal.deal_time)).execute()
            print(result)
            return result
        except Exception as e:
            raise StoreException('error adding deal')

class CompanyDealStore(BaseStore):
    def insert(self, deal_id, company_id):
        try:
            count = len(CompanyDeal.select())
            result = (CompanyDeal.insert(
                     id= count + 1,
                     deal_id= deal_id,
                     company_id= company_id)).execute()
            print(result)
            return result
        except Exception as e:
            #raise StoreException('error adding company')
            return 0

class DirectorsStore(BaseStore):
    def get_all(self):
        try:
            result = Directors.select() \
                .join(Employers)
            directors = []
            for man in result:
                directors.append(Director(man.id,
                                        man.employee_id.name,
                                        man.employee_id.age,
                                        man.employee_id.month_plan,
                                        man.region_id,
                                        man.employee_id.id))
            return directors
        except Exception as e:
            raise StoreException('error selecting directors')

    def get_region_by_id(self, id):
        try:
            query = (Employers.select(Regions.id.alias('id'), Regions.name.alias('name'),
                                       Regions.director_id.alias('director_id'),
                                       Regions.population.alias('population'),
                                       Regions.number_of_companies.alias('cmpn'))
                               .join(Directors)
                               .join(Regions, on=(Regions.director_id == Directors.id))
                               .where(Directors.id == id))
            result = []
            for row in query.dicts():
                result.append(Region(row['id'], row['name'], row['director_id'], row['population'], row['cmpn']))
            return result[0]
        except Exception as e:
            raise StoreException('error selecting region_id')

class AdministratorsStore(BaseStore):
    def get_all(self):
        try:
            result = Administrators.select() \
                .join(Employers)
            admins = []
            for man in result:
                admins.append(Administrator(man.id,
                                          man.employee_id.name,
                                          man.employee_id.age,
                                          man.employee_id.month_plan,
                                          man.director_id.id,
                                          man.district_id.id,
                                          man.employee_id.id))
            return admins
        except Exception as e:
            #raise StoreException('error selecting administrators')
            return 0

    def get_all_param(self, params):
        try:
            result = Administrators.select().where(params)
            return result
        except Exception as e:
            raise StoreException('error selecting administrators')

    def get_region_by_id(self, id):
        try:
            query = (Employers.select(Regions.id.alias('id'), Regions.name.alias('name'),
                                       Regions.director_id.alias('director_id'),
                                       Regions.population.alias('population'),
                                       Regions.number_of_companies.alias('cmpn'))
                               .join(Administrators)
                               .join(Districts)
                               .join(Regions)
                               .where(Administrators.id == id))
            result = []
            for row in query.dicts():
                result.append(Region(row['id'], row['name'], row['director_id'], row['population'], row['cmpn']))
            return result[0]
        except Exception as e:
            raise StoreException('error selecting region_id')

    def get_deals_of_managers(self, id):
        try:
            query = (Managers.select(Administrators.id.alias('id'), Companies.name.alias('company'), fn.SUM(Deals.deal_sum).alias('dealsum'))
                              .join(Companies)
                              .join(CompanyDeal)
                              .join(Deals)
                              .switch(Managers)
                              .join(Districts, on=(Districts.id == Managers.district_id))
                              .join(Administrators, on=(Administrators.id == Districts.administrator_id))
                              .where(Administrators.id == id, fn.date_part('month', Deals.deal_time) == 4, Deals.is_approved)
                              #.where(Administrators.id == id, fn.date_part('month', Deals.deal_time) == datetime.date.today().month)
                              .group_by(Companies.name, Administrators.id)
                              .order_by(fn.SUM(Deals.deal_sum)))
            result = []
            for row in query.dicts():
                result.append(CmpDealsSum(row['id'], row['company'], row['dealsum']))
            return result
        except Exception as e:
            #raise StoreException('error selecting manager deals')
            return 0

    def get_plans(self, region):
        try:
            query = (Employers.select(Administrators.id.alias('id'), Employers.name.alias('name'),
                                      Employers.month_plan.alias('plan'))
                                .join(Administrators)
                                .join(Districts)
                                .join(Regions)
                                .where(Regions.id == region.id))
            result = []
            for row in query.dicts():
                result.append(EmployersPlans(row['id'], row['name'], row['plan']))
            return result
        except Exception as e:
            raise StoreException('error selecting managers plans')