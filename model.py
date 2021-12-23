from repository import *
from entities import *
from random import randint

class BaseInserter():
    def insert(self):
        pass

class CompanyInserter(BaseInserter):
    def insert(self, company, app_user):
        with db:
            try:
                manager_id = app_user.id
                region = ManagersStore().get_region_by_id(manager_id)
                insert_company = AddCompany(company.name,
                                            region.id,
                                            manager_id,
                                            company.has_online,
                                            company.has_offline)
                result = CompaniesStore().insert(insert_company) # returns id of inserted company
                return result
            except:
                return 0

class DealInserter(BaseInserter):
    def insert(self, deal, company_name, dealsstore, companiesstore):
        with db:
            try:
                insert_deal = InsertDeal(deal.orderer_name,
                                            deal.deal_sum,
                                            deal.deal_type,
                                            True if randint(0, 1) else False,
                                            datetime.datetime.now().replace(microsecond=0, month=4))
                inserted_id = dealsstore.insert(insert_deal) # returns id of inserted deal
                company = companiesstore.get_by_name(company_name)
                company_id = company.id
                result = CompanyDealStore().insert(inserted_id, company_id)
                return insert_deal.is_approved
            except:
                return "Bad"

class BaseSelector():
    def find_all(self):
        pass

    def find_all_param(self, params):
        pass

    def find_by_id(self, id):
        pass

    def find_by_name(self, name):
        pass

class EmployeeSelector(BaseSelector):
    def find_all(self):
        with db:
            try:
                result = EmployersStore().get_all()
                return result
            except:
                return "Bad"

    def find_by_id(self, id):
        with db:
            try:
                result = EmployersStore().get_by_id(id)
                employer = Employee(result.id, result.name, result.age, result.month_plan, result.role, "", "")
                return employer
            except:
                return "Bad"

    def find_by_name(self, name):
        with db:
            try:
                result = EmployersStore().get_by_name(name)
                #employer = Employer(result.id, result.name, result.month_plan, result.role)
                return result
            except:
                return "Bad"

    def find_id_role(self, user):
        if user.role == "manager":
            manid = EmployersStore().get_manager_id(user)
        elif user.role == "administrator":
            manid = EmployersStore().get_administrator_id(user)
        elif user.role == "director":
            manid = EmployersStore().get_director_id(user)
        return manid

class ManagerSelector(BaseSelector):
    def find_by_name(self, name):
        with db:
            try:
                result = ManagersStore().get_by_name(name)
                return result
            except:
                return "Bad"

    def find_all(self):
        with db:
            try:
                result = ManagersStore().get_all()
                return result
            except:
                return "Bad"

    def find_deals(self, id):
        with db:
            try:
                result = ManagersStore().get_deals(id)
                return result
            except:
                return "Bad"

    def find_plans(self, region):
        with db:
            try:
                plans = ManagersStore().get_plans(region)
                result = []
                for manager in plans:
                    deals = ManagersStore().get_deals(manager.id)
                    sum = 0
                    for cmp in deals:
                        sum += cmp.deal_sum
                    result.append(EmployeePlanAchieve(manager.name, round(float(sum / manager.plan * 100), 0)))
                result = sorted(result, key= lambda man: man.plan_prcntg)
                return result
            except:
                raise DataError

class CompanySelector(BaseSelector):
    def find_by_name(self, name):
        with db:
            try:
                result = CompaniesStore().get_by_name(name)
                return result
            except:
                return "Bad"

    def find_all(self):
        with db:
            try:
                result = CompaniesStore().get_all()
                return result
            except:
                return "Bad"


class DealSelector(BaseSelector):
    def find_all(self):
        with db:
            try:
                result = DealsStore().get_all()
                return result
            except:
                return "Bad"

class DirectorSelector(BaseSelector):
    def find_by_name(self, name):
        with db:
            try:
                result = DirectorsStore().get_by_name(name)
                return result
            except:
                return "Bad"

    def find_all(self):
        with db:
            try:
                result = DirectorsStore().get_all()
                return result
            except:
                return "Bad"

    def find_plans(self, region):
        with db:
            try:
                plans_managers = ManagersStore().get_plans(region)
                plans_admins = AdministratorsStore().get_plans(region)
                result = []
                for admin in plans_admins:
                    deals = AdministratorsStore().get_deals_of_managers(admin.id)
                    sum = 0
                    for cmp in deals:
                        sum += cmp.deal_sum
                    result.append(EmployeePlanAchieve(admin.name, round(float(sum / admin.plan * 100), 0)))
                for manager in plans_managers:
                    deals = AdministratorsStore().get_deals_of_managers(manager.id)
                    sum = 0
                    for cmp in deals:
                        sum += cmp.deal_sum
                    result.append(EmployeePlanAchieve(manager.name, round(float(sum / manager.plan * 100), 0)))
                result = sorted(result, key= lambda man: man.plan_prcntg)
                return result
            except:
                raise DataError

    def find_deals_approve(self, region):
        with db:
            try:
                approved_deals = DealsStore().get_approved_deals_by_region(region)
                all_deals = DealsStore().get_deals_by_region(region)
                result = []
                for deal in all_deals:
                    all_cnt = deal.count
                    appr_cnt = 0
                    for j in approved_deals:
                        if deal.id == j.id:
                            appr_cnt = j.count
                    result.append(CmpApprove(deal.name, round(float(appr_cnt / all_cnt * 100), 0)))
                result = sorted(result, key= lambda company: company.approve_prcntg)
                return result
            except:
                return "Bad"

class AdministratorSelector(BaseSelector):
    def find_by_name(self, name):
        with db:
            try:
                result = AdministratorsStore().get_by_name(name)
                return result
            except:
                return "Bad"

    def find_all(self):
        with db:
            try:
                result = AdministratorsStore().get_all()
                return result
            except:
                raise DataError

    def find_plans(self, region):
        with db:
            try:
                plans = AdministratorsStore().get_plans(region)
                result = []
                for admin in plans:
                    deals = AdministratorsStore().get_deals_of_managers(admin.id)
                    sum = 0
                    for cmp in deals:
                        sum += cmp.deal_sum
                    result.append(EmployeePlanAchieve(admin.name, round(float(sum / admin.plan * 100), 0)))
                result = sorted(result, key= lambda man: man.plan_prcntg)
                return result
            except:
                raise DataError

class RegionSelector(BaseSelector):
    def find_by_name(self, name):
        with db:
            try:
                result = RegionsStore().get_by_name(name)
                return result
            except:
                raise DataError

    def find_all(self):
        with db:
            try:
                result = RegionsStore().get_all()
                return result
            except:
                return "Bad"

    def find_by_manager_id(self, id):
        with db:
            try:
                result = ManagersStore().get_region_by_id(id)
                return result
            except:
                raise DataError

    def find_by_admin_id(self, id):
        with db:
            try:
                result = AdministratorsStore().get_region_by_id(id)
                return result
            except:
                raise DataError

    def find_by_director_id(self, id):
        with db:
            try:
                result = DirectorsStore().get_region_by_id(id)
                return result
            except:
                raise DataError

class DistrictSelector(BaseSelector):
    def find_by_name(self, name):
        with db:
            try:
                result = DistrictsStore().get_by_name(name)
                return result
            except:
                return "Bad"

    def find_all(self):
        with db:
            try:
                result = DistrictsStore().get_all()
                return result
            except:
                return "Bad"


