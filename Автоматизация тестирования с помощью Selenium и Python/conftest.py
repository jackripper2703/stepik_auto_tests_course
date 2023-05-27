import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()



@pytest.fixture(scope="function")
def register(driver):
    input1 = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Gordon")
    input2 = driver.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Freeman")
    input3 = driver.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("gordon@freem.an")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(2)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = str(welcome_text_elt.text)
    return welcome_text