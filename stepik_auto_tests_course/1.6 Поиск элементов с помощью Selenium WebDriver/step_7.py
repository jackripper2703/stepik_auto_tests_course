import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
try:
    inputs = browser.find_elements(By.CSS_SELECTOR,"input")
    for i in inputs:
        i.send_keys("1")
    submit = browser.find_element(By.CSS_SELECTOR, "button")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()