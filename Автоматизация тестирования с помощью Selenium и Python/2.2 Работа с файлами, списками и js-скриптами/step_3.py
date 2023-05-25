import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

# Ссылка на которую нам нужно перейти
link = "https://suninjuly.github.io/selects1.html"
driver.get(link)

def summ_result():
    num1 = driver.find_element(By.CSS_SELECTOR,"#num1").text
    num2 = driver.find_element(By.CSS_SELECTOR,"#num2").text
    summ = int(num1) + int(num2)
    return summ

def select_click():
    select_element = driver.find_element(By.CSS_SELECTOR,"#dropdown")
    select_result = Select(select_element)
    select_result.select_by_visible_text(str(summ_result()))

def click_for_submit():
    button_submit = driver.find_element(By.CSS_SELECTOR,"[type^=su]")
    button_submit.click()

def start():
    select_click()
    click_for_submit()
    time.sleep(5)

start()

