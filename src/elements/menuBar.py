from src.elements.element import BasePageElement
from selenium.webdriver.common.by import By


class MenuBar(BasePageElement):

    MENU_BLOCK = (By.XPATH, "//div[contains(@class,'navbar ng-scope')]")
    SEARCH_CODE = (By.XPATH, "//a[@ui-sref='subNavBar.reinbursation.code']")
    SEARCH_DISPENSES = (By.XPATH, "//a[@ui-sref='subNavBar.reinbursation.dispenses']")
    MESSAGES = (By.XPATH, "//a[@ui-sref='system.messages']")
    SETTINGS = (By.XPATH, "//a[@ui-sref='system.setups']")
    EXIT = (By.XPATH, "//a[@ng-show='ctl.allowByRole(ctl.closeButton)']")

    def __init__(self, driver):
        self.driver = driver

    def menu_block_is_loaded(self):
        self.element_visible(self.MENU_BLOCK)
        return self

    def click_exit(self):
        self.element_click(self.EXIT)
        return self

    def click_dispense_report(self):
        self.element_click(self.SEARCH_DISPENSES)
        return self

    def click_messages(self):
        return self.element_click(self.MESSAGES)

    def click_settings(self):
        return self.element_click(self.SETTINGS)

    def click_search_code(self):
        return self.element_click(self.SEARCH_CODE)