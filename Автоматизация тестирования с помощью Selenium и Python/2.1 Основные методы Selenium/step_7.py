import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")

# Берем цифру из сундука и подставляем в формулу для вычесления данных
chest = calc((driver.find_element(By.CSS_SELECTOR, "img")).get_attribute("valuex"))

# Прокидуем данное число в строку ввода
textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(chest)

# Ставим отметку в чекбоксе
check_box = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
check_box.click()

# Ставим отметку в чекбоксе
radio = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
radio.click()

# Жмем кнопку "Submit"
time.sleep(2)
submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
submit.click()

time.sleep(10)
