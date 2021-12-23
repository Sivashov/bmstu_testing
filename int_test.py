import test
import unittest
from unittest.suite import TestSuite
from unittest.mock import patch
from controller import *
import view
import cProfile
import test as unittests


class TestPlotManagerPlan(unittest.TestCase):
    @patch('view.Interface')
    def test_plot(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("a.vasechkin1", "123")

        # act
        result = self.controller.plot_manager_plan(view_mock)
        self.controller.disconnect()

        # assert
        self.assertNotEqual(type(result), str)

class PlotManagerPlanTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestPlotManagerPlan))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestPlotAdminPlan(unittest.TestCase):
    @patch('view.Interface')
    def test_plot(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("v.ivanov682", "123")

        # act
        result = self.controller.plot_admin_plan(view_mock)
        self.controller.disconnect()

        # assert
        self.assertNotEqual(type(result), str)

class PlotAdminPlanTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestPlotAdminPlan))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestPlotDirectorPlan(unittest.TestCase):
    @patch('view.Interface')
    def test_plot(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("a.petrov1021", "123")

        # act
        result = self.controller.plot_director_plan(view_mock)
        self.controller.disconnect()

        # assert
        self.assertNotEqual(type(result), str)

class PlotDirectorPlanTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestPlotDirectorPlan))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestPlotManagerDeals(unittest.TestCase):
    @patch('view.Interface')
    def test_plot(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("a.petrov1021", "123")

        # act
        result = self.controller.plot_manager_deals(view_mock)
        self.controller.disconnect()

        # assert
        self.assertNotEqual(type(result), str)

class PlotManagerDealsTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestPlotManagerDeals))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestPlotDealsApprove(unittest.TestCase):
    @patch('view.Interface')
    def test_plot(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("a.petrov1021", "123")

        # act
        result = self.controller.plot_deals_approve(view_mock)
        self.controller.disconnect()

        # assert
        self.assertNotEqual(type(result), str)

class PlotDealsApproveTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestPlotDealsApprove))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestInsertCompany(unittest.TestCase):
    @patch('model.CompanyInserter.insert', return_value=True)
    def test_insert(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("v.ivanov682", "123")
        company = Company("Test Company", True, True)

        # act
        result = self.controller.insert_company(company)
        self.controller.disconnect()

        # assert
        CompanyInserter.insert.assert_called()
        self.assertNotEqual(type(result), str)

class InsertCompanyTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestInsertCompany))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class TestInsertDeal(unittest.TestCase):
    @patch('model.DealInserter.insert', return_value=True)
    def test_insert(self, view_mock):

        # arrange
        self.controller = Controller()
        self.controller.authorizate("v.ivanov682", "123")
        company = "Some Company"
        deal = InpDeal("Tester", 100000, 'online')

        # act
        result = self.controller.insert_deal(deal, company)
        self.controller.disconnect()

        # assert
        DealInserter.insert.assert_called()
        self.assertNotEqual(type(result), str)

class InsertDealTestClass():
    # arrange
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestInsertDeal))

    def start_testing(self):
        #print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)


class BaseIntegrationTestClass():
    def __init__(self):
        #mywin = Interface(self.controller)

        self.test_classes = [PlotManagerPlanTestClass(), PlotAdminPlanTestClass(), PlotDirectorPlanTestClass(),
                             PlotDealsApproveTestClass(), InsertCompanyTestClass(), InsertDealTestClass()]
        for i in self.test_classes:
            i.make_suite()

    def do_tests(self):
        #self.ts.start_testing()
        for i in self.test_classes:
            i.start_testing()

#--------------------------------------------------------------------------------------------------------------

def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper



class TestE2eManager(unittest.TestCase):
    @patch('view.Interface')
    @patch('statistics.PlotCanvas.plot_plan', return_value=False)
    def test_simple(self, plot_plan_mock, view_mock):

        # arrange
        controller = Controller()
        login = "a.vasechkin1"
        password = "123"
        view_t = ConsoleView(controller)

        # act
        controller.authorizate(login, password)

        # assert
        self.assertEqual(controller.user.name, "Aleksandr Vasechkin")

        # act
        result = controller.find_region_plans_manager()

        # assert
        self.assertNotEqual(type(result), str)
        self.assertEqual(len(result), 8)

        # act
        result = controller.plot_manager_plan(view_mock)

        # assert
        self.assertNotEqual(type(result), str)
        self.assertEqual(len(result), 8)

        controller.disconnect()

class BaseTestE2eManager(unittest.TestCase):
    def __init__(self):
        self.suite = TestSuite()
        self.tests = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity=3)

    def make_suite(self):
        self.suite.addTests(self.tests.loadTestsFromTestCase(TestE2eManager))

    def testMany(self, count=30):
        errorCount = 0
        t = TestE2eManager()
        for i in range(1, count):
            try:
                t.test_simple()
            except:
                errorCount += 1
        print(f'E2E test count errors: {errorCount}')

    def start_testing(self):
        # print("count of tests: " + str(self.suite.countTestCases()) + "\n")
        self.runner.run(self.suite)





def main():
    unittests.main()
    
    t = BaseIntegrationTestClass()
    t.do_tests()

    te = BaseTestE2eManager()
    te.make_suite()
    te.start_testing()
    te.testMany()
    return

if __name__ == "__main__":
    main()
