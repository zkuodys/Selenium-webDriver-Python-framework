from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """Class for Home page locators."""

    freeTrialButton = (By.XPATH, "//a[contains(text(),'Free trial')]")


class TrialPageLocators(object):
    """Class for Free Trial page locators."""

    supplierButton = (By.XPATH, "//a[contains(text(),'a supplier')]")


class SupplierPageLocators(object):
    """Class for Supplier page locators."""

    companyNameInput = (By.XPATH, "//input[@placeholder='My travel company']")
    companyEmailInput = (By.XPATH, "//input[@placeholder='bookings@mytravelcompany.com']")
    companyAddress = (By.XPATH, "//input[@placeholder='Search for address...']")
    businessCategoryDropDown = (By.XPATH, "//div[@id='react-select-2--value']")
    businessCategoryOption1 = (By.XPATH, "//span[contains(text(),'Sightseeing Tours')]")
    companyWebsite = (By.XPATH, "//input[@placeholder='http://example.com']")
    companyNumber = (By.XPATH, "//input[@placeholder='+1-541-754-3010']")
    whereDidYouHearAboutUs = (
        By.XPATH, "//div[@class='BokunTextInput form-group signupSource is-missing']//div//input[@type='text']")
