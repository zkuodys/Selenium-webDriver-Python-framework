from support.locators import SupplierPageLocators
from support.page_base import BasePage
from support import users


class SupplierPage(BasePage):
    """Class for storing methods that are used in Supplier page"""

    def enter_company_name(self, company):
        self.send_keys(users.get_user(company)["company name"], *SupplierPageLocators.companyNameInput)

    def enter_company_email(self, company):
        self.send_keys(users.get_user(company)["email"], *SupplierPageLocators.companyEmailInput)

    def enter_company_address(self, company):
        self.send_keys(users.get_user(company)["address"], *SupplierPageLocators.companyAddress)

    def enter_company_website(self, company):
        self.send_keys(users.get_user(company)["website"], *SupplierPageLocators.companyWebsite)

    def enter_company_phone_number(self, company):
        self.send_keys(users.get_user(company)["phone"], *SupplierPageLocators.companyNumber)

    def enter_info(self, company):
        self.send_keys(users.get_user(company)["info"], *SupplierPageLocators.whereDidYouHearAboutUs)

    def select_business_category(self, keys):
        pass

    def enter_company_information(self, company):
        self.enter_company_name(company)
        self.enter_company_email(company)
        self.enter_company_address(company)
        self.enter_company_website(company)
        self.enter_company_phone_number(company)
        self.enter_info(company)
