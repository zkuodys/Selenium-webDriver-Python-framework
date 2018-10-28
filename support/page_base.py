from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage(object):
    """This class is base for all Pages and stores methods that are reused in other pages."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_loader_to_finish(self, timeout):
        timeout = timeout
        try:
            element_present = ec.presence_of_element_located((By.XPATH, "//div[contains(@style,'display')]"))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print "Timed out waiting for page to load"

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def send_keys(self, keys, *locator):
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(keys)
