from models import *
from repository import *
from model import *

def main():
    try:
        db.init('BankStructure', user='postgres',
                password='forest123ry',
                host='localhost',
                port='5432')
        db.connect()
        print("Connected as sysadmin.\n")
    except:
        raise DataError

    error_count = 0

    #company = Company("Test", "yes", "yes")
    #user = User("login", "password", "tester", 1, "tester")
    manager_id = 1
    region_id = 1
    insert_company = AddCompany("TestCompany",
                                region_id,
                                manager_id,
                                False,
                                False)
    result = CompaniesStore().insert(insert_company)
    if not result:
        error_count += 1

    result = CompaniesStore().get_by_name("TestCompany")
    if not result:
        error_count += 1

    result = CompaniesStore().change_conds("TestCompany", ["no", "no"])
    if not result:
        error_count += 1

    result = CompaniesStore().delete("TestCompany")
    if not result:
        error_count += 1

    if error_count:
        print("Some errors occured.")
    else:
        print("OK")





if __name__ == "__main__":
    main()