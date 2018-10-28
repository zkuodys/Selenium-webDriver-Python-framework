import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.supplier_page import SupplierPage


class FirstTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(url='http://bokun.io/')

    def test_01(self):
        driver = self.driver
        _homePage = HomePage(driver)
        _supplierPage = SupplierPage(driver)

        _homePage.wait_for_loader_to_finish(timeout=10)
        _homePage.click_free_trial_button()

        _supplierPage.wait_for_loader_to_finish(timeout=10)
        _supplierPage.click_supplier_button()

    def tearDown(self):
        self.driver.quit()
