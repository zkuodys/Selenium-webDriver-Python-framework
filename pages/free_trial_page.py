from support.locators import TrialPageLocators
from support.page_base import BasePage


class FreeTrialPage(BasePage):
    """Class for storing methods that are used in Free Trial page"""

    def click_supplier_button(self):
        self.find_element(*TrialPageLocators.supplierButton).click()
