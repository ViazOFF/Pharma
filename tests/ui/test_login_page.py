import os
import pytest

import src.elements.menuBar
from src.pages.loginPage import LoginPage


@pytest.mark.usefixtures("chrome_login_page")
@pytest.mark.usefixtures("firefox_login_page")
class TestLoginPage:
    LOGIN = os.environ.get("PHARMA_LOGIN")
    PASSWORD = os.environ.get("PHARMA_PASSWORD")
    FAIL_NUMBER = "0123456789"

    # @allure.title("Check title")
    def test_load_page(self):
        login_page = LoginPage(self.driver)
        assert login_page.at_page(), "Title is wrong"

    # @allure.title("Check fail login and password click Submit")
    @pytest.mark.parametrize("login, password, message",
                             [
                                 ("admin", "", "Введіть ваш пароль"),
                                 ("", "wrongPass", "Введіть ваш номер телефону"),
                                 ("wrongLogin", "changeme", "Невірний логін або пароль"),
                                 ("1234567890", "admin", "Невірний логін або пароль"),
                                 ("admin", "admin", "Невірний логін або пароль"),
                                 ("chief", "chief", "Невірний логін або пароль"),
                             ]
                             )
    def test_enter_submit_fail_login_data(self, login, password, message):
        login_page = LoginPage(self.driver)
        login_page.set_login(login)
        login_page.set_password(password)
        login_page.click_submit()
        assert login_page.error_has_message(message), "Has no popup"

    # @allure.title("Check fail login and password press Enter")
    @pytest.mark.parametrize("login, password, message",
                             [
                                 ("admin", "", "Введіть ваш пароль"),
                                 ("", "wrongPass", "Введіть ваш номер телефону"),
                                 ("wrongLogin", "changeme", "Невірний логін або пароль"),
                                 ("1234567890", "admin", "Невірний логін або пароль"),
                                 ("admin", "admin", "Невірний логін або пароль"),
                                 ("chief", "chief", "Невірний логін або пароль"),
                             ]
                             )
    def test_press_enter_fail_login_data(self, login, password, message):
        login_page = LoginPage(self.driver)
        login_page.set_login(login)
        login_page.set_password(password)
        login_page.press_enter()
        assert login_page.error_has_message(message), "Has no popup"

    def test_lost_password_and_return(self):
        login_page = LoginPage(self.driver)
        login_page.set_login(self.FAIL_NUMBER)
        login_page.press_forget_password()
        assert login_page.save_phone_number_in_forget_input(self.FAIL_NUMBER), "Has no phone phone in input"
        login_page.click_back_in_forget_pass()
        login_page.click_submit()
        assert login_page.error_has_message("Введіть ваш пароль"), "Has no popup 'Введіть ваш пароль'"

    # @allure.title("first login test")
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_login_ok_click_submit(self):
        login_page = LoginPage(self.driver)
        menu = src.elements.menuBar.MenuBar(self.driver)
        login_page.set_login(self.LOGIN)
        login_page.set_password(self.PASSWORD)
        login_page.click_submit()
        assert menu.menu_block_is_loaded(), "Has no menu bar"

   # @allure.title("Test to be skipped")
    @pytest.mark.feature
    @pytest.mark.P1
    @pytest.mark.ui
    @pytest.mark.skip(reason="NMB-12222 User authorization is blocked by advertisement")
    def test_to_be_skipped(self):
        # TODO: implement this test
        pass
