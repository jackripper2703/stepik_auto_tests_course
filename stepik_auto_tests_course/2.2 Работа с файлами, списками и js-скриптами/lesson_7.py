import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_num = driver.find_element(By.CSS_SELECTOR,"#input_value")
result = calc(x_num.text)

textarea = driver.find_element(By.CSS_SELECTOR, "input")
textarea.send_keys(result)

check_box = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
driver.execute_script("return arguments[0].scrollIntoView(true);", check_box)
check_box.click()

radio = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()

time.sleep(15)