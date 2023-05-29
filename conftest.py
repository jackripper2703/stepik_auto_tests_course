import pytest
import time
import math
from config import loggin, password
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        browser = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver.exe", options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# link = [
#     "https://stepik.org/lesson/236895/step/1",
#     "https://stepik.org/lesson/236896/step/1",
#     "https://stepik.org/lesson/236897/step/1",
#     "https://stepik.org/lesson/236898/step/1",
#     "https://stepik.org/lesson/236899/step/1",
#     "https://stepik.org/lesson/236903/step/1",
#     "https://stepik.org/lesson/236904/step/1",
#     "https://stepik.org/lesson/236905/step/1"
# ]
#
#
# @pytest.fixture(params=link)
# def driver(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(options=options)
#     driver.get(request.param)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture()
# def auth(driver):
#     auth = driver.find_element(By.CSS_SELECTOR, "[href$='/step/1?auth=login']")
#     auth.click()
#
#     driver.find_element(By.CSS_SELECTOR, "[name='login']").send_keys(loggin)
#     driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#
# @pytest.fixture()
# def answer(driver):
#     answer = str(math.log(int(time.time())))
#     textarea = driver.find_element(By.CSS_SELECTOR, "textarea")
#     disabled = textarea.get_attribute("disabled")
#     if not disabled:
#         text_value = textarea.get_attribute('value')
#         if text_value:
#             textarea.clear()
#             textarea.send_keys(answer)
#         else:
#             textarea.send_keys(answer)
#
# @pytest.fixture()
# def correct(driver):
#     checkout = driver.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
#     text_answer = checkout.text
#     assert text_answer == "Correct!", print(text_answer)
#
#
# @pytest.fixture(scope="function")
# def register(driver):
#     input1 = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
#     input1.send_keys("Gordon")
#     input2 = driver.find_element(By.CSS_SELECTOR, ".first_block .second")
#     input2.send_keys("Freeman")
#     input3 = driver.find_element(By.CSS_SELECTOR, ".first_block .third")
#     input3.send_keys("gordon@freem.an")
#     button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     button.click()
#     time.sleep(2)
#     welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
#     welcome_text = str(welcome_text_elt.text)
#     return welcome_text
