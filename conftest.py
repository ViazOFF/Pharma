import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.android.webdriver import WebDriver


@pytest.fixture(name="chrome_login_page")
def get_driver(request):
    driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://pharmacy-test-preprod.newmedicine.com.ua/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


@pytest.fixture(name="firefox_login_page")
def get_driver(request):
    driver: WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get("http://pharmacy-test-preprod.newmedicine.com.ua/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     marker = item.get_closest_marker("ui")
#     if marker:
#         if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
#             try:
#                 allure.attach(item.instance.driver.get_screenshot_as_png(),
#                               name=item.name,
#                               attachment_type=allure.attachment_type.PNG)
#             except Exception as e:
#                 print(e)
