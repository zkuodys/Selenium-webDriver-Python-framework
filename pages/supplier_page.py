from support.locators import SupplierPageLocators
from support.page_base import BasePage


class SupplierPage(BasePage):
    """Class for storing methods that are used in Supplier page"""

    def enter_company_name(self, text):
        self.send_keys(text, *SupplierPageLocators.companyNameInput)

    def enter_company_email(self, text):
        self.send_keys(text, *SupplierPageLocators.companyEmailInput)

    def enter_company_address(self, text):
        self.send_keys(text, *SupplierPageLocators.companyAddress)

    def enter_company_website(self, text):
        self.send_keys(text, *SupplierPageLocators.companyWebsite)

    def enter_company_phone_number(self, text):
        self.send_keys(text, *SupplierPageLocators.companyNumber)

    def enter_hear(self, text):
        self.send_keys(text, *SupplierPageLocators.whereDidYouHearAboutUs)
