import allure
from selenium.webdriver.common.keys import Keys
from src.pages.basePageObject import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
#    driver = None

    # login page locators
    LOGIN_FORM = (By.XPATH, "//form[@class='conf auth wide ng-pristine ng-valid ng-scope']")
    SUBMIT = (By.XPATH, "//button[@class='btn btn-green long btn-inline']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='message ng-binding'][contains(.,'Введіть ваш пароль')]")
    LOGIN_INPUT = (By.NAME, "EQ_login_auth")
    PASSWORD_INPUT = (By.NAME, "EQ_password_auth")
    LINK_FORGET_PASSWORD = (By.XPATH, "//div[contains(@ng-click,'ctl.ForgetPass()')]")
    FORGET_PASSWORD_FORM = (By.XPATH, "//form[contains(@ng-submit,'ctl.ForgetPassSubmit()')]")
    PHONE_INPUT_FORGET_PASSWORD = (By.XPATH, "//input[contains(@placeholder,'Введіть ваш телефон')]")
    FORGET_PASSWORD_BUTTON_NEXT = (By.XPATH, "//div[@class='btn-ico confirm'][contains(.,'Далі')]")
    FORGET_PASSWORD_BUTTON_BACK = (By.XPATH, "//div[@class='btn-ico short cancel dark'][contains(.,'Назад')]")

    # login page init

    def __init__(self, driver):
        self.driver = driver

    # Login page method
    def open(self):
        self.driver.get("https://pharmacy-test-preprod.newmedicine.com.ua/")
        return self

    def click_submit(self):
        self.element_click(self.SUBMIT)
        return self

    def take_error_message(self):
        self.element_visible(self.ERROR_MESSAGE)
        return self

    def set_login(self, login):
        self.send_in_input(self.LOGIN_INPUT, login)
        return self

    def set_password(self, password):
        self.send_in_input(self.PASSWORD_INPUT, password)
        return self

    def press_enter(self):
        self.send_in_input(self.PASSWORD_INPUT, Keys.ENTER)
        return self

    def press_forget_password(self):
        self.element_click(self.LINK_FORGET_PASSWORD)
        return self

    def forget_pass_input(self):
        self.element_visible(self.PHONE_INPUT_FORGET_PASSWORD)
        return self

    def click_back_in_forget_pass(self):
        self.element_click(self.FORGET_PASSWORD_BUTTON_BACK)
        return self

    def pop_ap_message_click(self):
        self.element_click(self.ERROR_MESSAGE)
        return self

    def clear_login_input(self):
        self.send_in_input(self.LOGIN_INPUT, Keys.CONTROL + "a")
        self.send_in_input(self.LOGIN_INPUT, Keys.DELETE)
        return self

    # method to check UI elements for assert

    def at_page(self):
        return "Поліклініка без черг" in self.driver.title

    def error_has_message(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='message ng-binding'][contains(.,'" + text + "')]")))

    def save_phone_number_in_forget_input(self, number):
        element = self.get_element_attribute(self.PHONE_INPUT_FORGET_PASSWORD, "value")
        return number in element
