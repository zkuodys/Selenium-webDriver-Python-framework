import unittest
from selenium import webdriver


class FirstTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(url='http://bokun.io/')

    def test(self):
        pass

    def tearDown(self):
        self.driver.quit()
