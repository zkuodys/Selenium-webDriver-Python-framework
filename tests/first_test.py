import time
import unittest

from selenium import webdriver

from pages.home_page import HomePage
from pages.free_trial_page import FreeTrialPage
from pages.supplier_page import SupplierPage


class FirstTest(unittest.TestCase):
    """Test opens 'http://bokun.io/', goes to Free Trial and tries to create a supplier account. Does not fill in last 
      required field. Check that: 
        - alert message 'There is a problem with some of the fields' is visible
        -it is not possible to continue:
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(url='http://bokun.io/')

    def test_01(self):
        driver = self.driver
        _homePage = HomePage(driver)
        _trialPage = FreeTrialPage(driver)
        _supplierPage = SupplierPage(driver)

        _homePage.wait_for_loader_to_finish(timeout=10)
        _homePage.click_free_trial_button()

        _trialPage.wait_for_loader_to_finish(timeout=10)
        _trialPage.click_supplier_button()

        _supplierPage.enter_company_name('Made Up Company')
        _supplierPage.enter_company_email('moc@gmail.com')
        _supplierPage.enter_company_address('Vilnius, Lithuania')
        _supplierPage.enter_company_website('http://www.muc.com')
        _supplierPage.enter_company_phone_number('+37060501010')
        _supplierPage.enter_hear('hahah')

        time.sleep(300)

        assert 'There is a problem with some of the fields:' in driver.page_source

    def tearDown(self):
        self.driver.quit()
