import unittest
from unittest.suite import TestSuite
from unittest.mock import patch
from controller import *

class TestRegionsStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = RegionsStore().get_all()

        # assert
        self.assertTrue(result)

class RegionsStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestRegionsStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestDistrictsStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = DistrictsStore().get_all()

        # assert
        self.assertTrue(result)

class DistrictsStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDistrictsStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestEmployersStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = EmployersStore().get_all()

        # assert
        self.assertTrue(result)

    def test_get_by_id(self):
        # arrange
        employee_id = 1
        employee_name = "Aleksandr Vasechkin"

        # act
        result = EmployersStore().get_by_id(employee_id)

        # assert
        self.assertEqual(result.name, employee_name)

    def test_get_by_name(self):
        # arrange
        employee_id = 1
        employee_name = "Aleksandr Vasechkin"

        # act
        result = EmployersStore().get_by_name(employee_name)

        # assert
        self.assertEqual(result.get().id, employee_id)

class EmployersStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestEmployersStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestManagersStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = ManagersStore().get_all()

        # assert
        self.assertTrue(result)

    def test_get_by_id(self):
        # arrange
        manager_id = 1
        employee_id = 1

        # act
        result = ManagersStore().get_by_id(manager_id).employee_id.id
        # assert
        self.assertEqual(result, employee_id)

    def test_get_by_name(self):
        # arrange
        id = 1
        name = "Aleksandr Vasechkin"

        # act
        result = ManagersStore().get_by_name(name)[0].id

        # assert
        self.assertEqual(result, id)

class ManagersStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestManagersStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestCompaniesStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = CompaniesStore().get_all()

        # assert
        self.assertTrue(result)

    @patch('repository.CompaniesStore.insert', return_value=True)
    def test_insert(self, insert):
        # arrange
        company = Company("Some Name", True, False)

        # act
        result = CompaniesStore().insert(company)
        # assert
        self.assertTrue(result)

    @patch('repository.CompaniesStore.delete', return_value=1)
    def test_delete(self, delete):
        # arrange
        company = "Some Name"

        # act
        result = CompaniesStore().delete(company)
        # assert
        self.assertTrue(result)

class CompaniesStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestCompaniesStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestDealsStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = DealsStore().get_all()

        # assert
        self.assertTrue(result)

    @patch('repository.DealsStore.insert', return_value=True)
    def test_insert(self, insert):
        # arrange
        deal = InpDeal("Some Name", 300000, "online")

        # act
        result = DealsStore().insert(deal)
        # assert
        self.assertTrue(result)

    def test_get_deals_by_region(self):

        # arrange
        region = Region(4, "Sankt-Peterburg", 4, 5383890, 10)

        # act
        result = DealsStore().get_deals_by_region(region)

        # assert
        self.assertEqual(len(result), 9)

class DealsStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDealsStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestCompanyDealStore(unittest.TestCase):

    @patch('repository.CompanyDealStore.insert', return_value=True)
    def test_insert(self, insert):
        # arrange
        deal_id = 10000
        company_id = 10

        # act
        result = CompanyDealStore().insert(deal_id, company_id)

        # assert
        self.assertTrue(result)

class CompanyDealStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestCompanyDealStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestDirectorsStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = DirectorsStore().get_all()

        # assert
        self.assertTrue(result)

    def test_get_region_by_id(self):
        # arrange
        director_id = 1

        # act
        result = DirectorsStore().get_region_by_id(director_id).name

        # assert
        self.assertEqual(result, "Moskva")

class DirectorsStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDirectorsStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestAdminsStore(unittest.TestCase):
    def test_get_all_common(self):

        # arrange

        # act
        result = AdministratorsStore().get_all()

        # assert
        self.assertTrue(result)

    def test_get_region_by_id(self):
        # arrange
        admin_id = 1

        # act
        result = AdministratorsStore().get_region_by_id(admin_id).name

        # assert
        self.assertEqual(result, "Moskva")

    def test_get_deals(self):
        # arrange
        admin_id = 1

        # act
        result = AdministratorsStore().get_deals_of_managers(admin_id)

        # assert
        self.assertTrue(result)

class AdminsStoreTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestAdminsStore))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)

'''---------------------------------------------------------------------------------------'''


class TestCompanyInserter(unittest.TestCase):

    @patch('model.CompanyInserter.insert', return_value=True)
    def test_insert(self, insert):
        # arrange
        company = Company("Some Name", True, False)
        app_user = User("a.vasechkin1", "123", "manager", 1, "Some Name")

        # act
        result = CompanyInserter().insert(company, app_user)

        # assert
        self.assertTrue(result)

class CompanyInserterTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestCompanyInserter))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class ObjectMotherDeal():
    def createDealSimple(self):
        return InpDeal("Some Name", 100000, "online")

    def createDealWithNameSum(self, name, sum):
        return InpDeal(str(name), sum, "online")

    def createDealWithName(self, name):
        return InpDeal(str(name), 100000, "online")

class TestDealInserter(unittest.TestCase):

    @patch('model.DealsStore')
    @patch('model.CompaniesStore')
    def test_insert(self, CompaniesStoreMock, DealsStoreMock):
        # arrange
        #deal = InpDeal("Some Name", 100000, "online")
        deal = ObjectMotherDeal().createDealWithNameSum("Some Name", 120000)
        company = "Some Company"

        # act
        result = DealInserter().insert(deal, company, DealsStoreMock, CompaniesStoreMock)

        # assert
        DealsStoreMock.insert.assert_called()
        CompaniesStoreMock.get_by_name.assert_called_with(company)
        self.assertNotEqual(result, "Bad")

class DealInserterTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDealInserter))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestEmployeeSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = EmployeeSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_by_id(self):
        # arrange
        test_id = 1

        # act
        result = EmployeeSelector().find_by_id(test_id)

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_by_name(self):
        # arrange
        name = "Aleksandr Vasechkin"

        # act
        result = EmployeeSelector().find_by_name(name)

        # assert
        self.assertNotEqual(result, "Bad")

class EmployeeSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestEmployeeSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestManagerSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = ManagerSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_by_name(self):
        # arrange
        name = "Aleksandr Vasechkin"

        # act
        result = ManagerSelector().find_by_name(name)

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_deals(self):
        # arrange
        test_id = 1

        # act
        result = ManagerSelector().find_deals(test_id)

        # assert
        self.assertNotEqual(result, "Bad")

class ManagerSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestManagerSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestCompanySelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = CompanySelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_by_name(self):
        # arrange
        name = "Monolit"

        # act
        result = CompanySelector().find_by_name(name)

        # assert
        self.assertNotEqual(result, "Bad")

class CompanySelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestCompanySelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestDealSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = DealSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

class DealSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDealSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestDirectorSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = DirectorSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_plans(self):
        # arrange
        region = Region(1, "Moskva", 1, 12615279, 6)

        # act
        result = (DirectorSelector().find_plans(region))[0].name
        # assert
        self.assertEqual(result, "Aleksandr Kolosov")

class DirectorSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDirectorSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestAdminSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = AdministratorSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_plans(self):
        # arrange
        region = Region(1, "Moskva", 1, 12615279, 6)

        # act
        result = (AdministratorSelector().find_plans(region))[0].name
        # assert
        self.assertEqual(result, "Evgeniya Pozdnyakova")

    def test_find_by_name(self):
        # arrange
        name = "Vasiliy Ivanov"

        # act
        result = AdministratorSelector().find_by_name(name)

        # assert
        self.assertNotEqual(result, "Bad")

class AdminSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestAdminSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestRegionSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = RegionSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_by_manager_id(self):
        # arrange
        test_id = 1

        # act
        result = RegionSelector().find_by_manager_id(test_id).name

        # assert
        self.assertEqual(result, "Moskva")

    def test_find_by_admin_id(self):
        # arrange
        test_id = 1

        # act
        result = RegionSelector().find_by_admin_id(test_id).name

        # assert
        self.assertEqual(result, "Moskva")

class RegionSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestRegionSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestDistrictSelector(unittest.TestCase):

    def test_find_all(self):
        # arrange

        # act
        result = DistrictSelector().find_all()

        # assert
        self.assertNotEqual(result, "Bad")

    def test_find_by_name(self):
        # arrange
        name = "East"

        # act
        result = DistrictSelector().find_by_name(name)
        a = [elem for elem in result if elem.name == "East"]

        # assert
        self.assertEqual(len(a), len(result))

class DistrictSelectorTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestDistrictSelector))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


'''---------------------------------------------------------------------------------------'''
class BaseTestClass():
    def __init__(self):
        self.controller = Controller()
        self.controller.logger = RoleLogger()
        self.controller.logger.basicConfig("logfile.txt")
        self.controller.authorizate("a.vasechkin1", "123")
        self.test_classes = [RegionsStoreTestClass(), DistrictsStoreTestClass(), EmployersStoreTestClass(),
                             ManagersStoreTestClass(), CompaniesStoreTestClass(), DealsStoreTestClass(),
                             CompanyDealStoreTestClass(), DirectorsStoreTestClass(), AdminsStoreTestClass(),
                             CompanyInserterTestClass(), DealInserterTestClass(), EmployeeSelectorTestClass(),
                             ManagerSelectorTestClass(), CompanySelectorTestClass(), DealSelectorTestClass(),
                             DirectorSelectorTestClass(), AdminSelectorTestClass(), RegionSelectorTestClass(),
                             DistrictSelectorTestClass()]
        for i in self.test_classes:
            i.make_suite()

    def do_tests(self):
        #self.ts.start_testing()
        for i in self.test_classes:
            i.start_testing()

    def disconnect(self):
        self.controller.disconnect()

def main():
    t = BaseTestClass()
    t.do_tests()
    t.disconnect()
    return

if __name__ == "__main__":
    main()