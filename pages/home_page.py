from support.locators import HomePageLocators
from support.page_base import BasePage


class HomePage(BasePage):
    """Class for storing methods that are used in Home page"""

    def click_free_trial_button(self):
        self.find_element(*HomePageLocators.freeTrialButton).click()
