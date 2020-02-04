from src.elements.element import BasePageElement
from selenium.webdriver.common.by import By


class ChiefMenuBar(BasePageElement):

    MENU_BLOCK = (By.XPATH, "//div[contains(@class,'navbar ng-scope')]")
    INSTITUTION = (By.XPATH, "//a[contains(.,'Заклад')]")
    DIVISION = (By.XPATH, "//a[@ui-sref='subNavBar.filials']")
    HR_DIVISION = (By.XPATH, "//a[@ui-sref='subNavBar.recorders']")
    PHARMACISTS = (By.XPATH, "//a[@ui-sref='subNavBar.doctors']")
    REPORTS = (By.XPATH, "//a[@ui-sref='subNavBar.dispensesReport']")
    MESSAGES = (By.XPATH, "//a[@ui-sref='system.messages']")
    CONTRACTS = (By.XPATH, "//a[@ui-sref='subNavBar.contracts']")
    SETTINGS = (By.XPATH, "//a[@ui-sref='system.setups']")
    EXIT = (By.XPATH, "//a[@ng-show='ctl.allowByRole(ctl.closeButton)']")

    def __init__(self, driver):
        self.driver = driver

    def menu_block_is_loaded(self):
        self.element_visible(self.MENU_BLOCK)
        return self

    def click_about_legal_entity(self):
        return self.element_click(self.INSTITUTION)

    def click_filials(self):
        self.element_click(self.DIVISION)
        return self

    def click_hr_division(self):
        self.element_click(self.HR_DIVISION)
        return self

    def click_pharmacists(self):
        self.element_click(self.PHARMACISTS)
        return self

    def click_reports(self):
        self.element_click(self.REPORTS)
        return self

    def click_messages(self):
        return self.element_click(self.MESSAGES)

    def click_contracts(self):
        return self.element_click(self.CONTRACTS)

    def click_settings(self):
        return self.element_click(self.SETTINGS)

    def click_exit(self):
        self.element_click(self.EXIT)
        return self
