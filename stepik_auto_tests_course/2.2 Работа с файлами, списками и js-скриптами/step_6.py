from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    # Берем цифру и подставляем в формулу для вычесления данных
    x_element = browser.find_element(By.CSS_SELECTOR, "label :nth-child(2)")
    y = calc(x_element.text)

    # Прокидуем данное число в строку ввода
    textarea = browser.find_element(By.CSS_SELECTOR, "#answer")
    textarea.send_keys(y)
    # Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
    # Эта команда проскроллит страницу на 100 пикселей вниз:
    browser.execute_script("window.scrollBy(0, 100);")
    # Ставим отметку в чекбоксе
    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_box.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    #.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Данный параметр передает js код,который скролит страницу так,что бы элемент button был в центре и не преграждался другими элементами
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()