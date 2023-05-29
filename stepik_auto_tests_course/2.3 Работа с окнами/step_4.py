import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")

button_c = driver.find_element(By.CSS_SELECTOR, "button[class$='btn-primary']")
button_c.click()
# Переключаемся на диалоговое окно Confirm
confirm_dialog = driver.switch_to.alert
# Подтверждаем Confirm
confirm_dialog.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.CSS_SELECTOR, "span[id='input_value']")
answer = calc(x_element.text)

input_math = driver.find_element(By.CSS_SELECTOR, "#answer")

input_math.send_keys(answer)

submit = driver.find_element(By.CSS_SELECTOR, "button[class$='btn-primary']")

submit.click()

time.sleep(10)