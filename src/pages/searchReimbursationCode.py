from src.pages.basePageObject import BasePage
from selenium.webdriver.common.by import By


class SearchReimbursationCode(BasePage):
#    driver = None

    # Search Page Locators
    LOGOUT_EHEALTH = (By.XPATH, "//a[contains(@ng-if,'ctl.isLoggedIn && ctl.showLogOut')]")
    INPUT_CODE = (By.XPATH, "//input[@name='code']")
    POPUP_MESSAGE = (By.XPATH, "//div[contains(@class,'message ng-binding')]")
    SEARCH_BUTTON = (By.XPATH, "//div[contains(@class,'btn-ico search')]")

    # Search Page init
    def __init__(self, driver):
        self.driver = driver

    def take_popup_message(self):
        self.element_visible(self.POPUP_MESSAGE)
        return self

    def set_recipe_code(self, code):
        self.send_in_input(self.INPUT_CODE, code)
        return self

    def click_submit(self):
        self.element_click(self.SEARCH_BUTTON)
        return self

    def check_login_ehealth(self):
        self.element_visible(self.LOGOUT_EHEALTH)
        return self

    def logout_ehealth(self):
        self.element_click(self.LOGOUT_EHEALTH)
        return self


