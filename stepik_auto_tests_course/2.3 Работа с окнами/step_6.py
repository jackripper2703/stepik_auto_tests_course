import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

trollface = driver.find_element(By.CSS_SELECTOR, "button")
trollface.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x = driver.find_element(By.CSS_SELECTOR, "#input_value")
answer = driver.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(calc(x.text))

submit = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
submit.click()
