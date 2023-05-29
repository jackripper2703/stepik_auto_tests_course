import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Берем цифру и подставляем в формулу для вычесления данных
x_element = driver.find_element(By.CSS_SELECTOR, "label :nth-child(2)")
y = calc(x_element.text)

# Прокидуем данное число в строку ввода
textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)
time.sleep(1)

# Ставим отметку в чекбоксе
check_box = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
check_box.click()
time.sleep(1)

# Ставим отметку в чекбоксе
radio = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
radio.click()
time.sleep(1)


# Жмем кнопку "Submit"
submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
submit.click()

time.sleep(15)