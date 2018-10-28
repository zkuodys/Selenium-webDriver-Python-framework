from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """Class for Home page locators."""

    freeTrialButton = (By.XPATH, "//a[contains(text(),'Free trial')]")


class TrialPageLocators(object):
    """Class for Free Trial page locators."""

    supplierButton = (By.XPATH, "//a[contains(text(),'a supplier')]")


class SupplierPageLocators(object):
    """Class for Supplier page locators."""