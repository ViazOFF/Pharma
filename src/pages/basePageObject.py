from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def element_click(self, locator):
        return WebDriverWait(self.driver, 10).until(ex_cond.element_to_be_clickable(locator)).click()

    def element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(ex_cond.visibility_of_element_located(locator))

    def send_in_input(self, locator, keys):
        inp = WebDriverWait(self.driver, 10).until(ex_cond.element_to_be_clickable(locator))
        return inp.send_keys(keys)

    def clear_input(self, locator):
        element = WebDriverWait(self.driver, 10).until(ex_cond.element_to_be_selected(locator))
        return element.clear()

    def get_text_in_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(ex_cond.visibility_of_element_located(locator))
        return element.text

    def get_element_attribute(self, locator, attr):
        element = WebDriverWait(self.driver, 10).until(ex_cond.visibility_of_element_located(locator))
        return element.get_attribute(attr)
