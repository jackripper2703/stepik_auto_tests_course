import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
link = ""
driver.get(link)
driver.implicitly_wait(10)
try:
    print(1)
finally:
    time.sleep(10)
    driver.quit()