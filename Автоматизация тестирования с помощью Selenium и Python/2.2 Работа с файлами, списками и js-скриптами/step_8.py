import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

FIRST_NAME = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
FIRST_NAME.send_keys("JACK")
LAST_NAME = driver.find_element(By.CSS_SELECTOR, '[name="lastname"]')
LAST_NAME.send_keys("RIPPER")
EMAIL = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
EMAIL.send_keys("sad.sadsad.sad@yandex.ru")
FILE = driver.find_element(By.CSS_SELECTOR, '#file')
FILE.send_keys("C:/environments/test/test.txt")
SUBMIT = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
SUBMIT.click()

time.sleep(10)