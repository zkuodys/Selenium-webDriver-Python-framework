from support.locators import TrialPageLocators
from support.page_base import BasePage


class SupplierPage(BasePage):
    """Class for storing methods that are used in Supplier page"""

    def click_supplier_button(self):
        self.find_element(*TrialPageLocators.supplierButton).click()
