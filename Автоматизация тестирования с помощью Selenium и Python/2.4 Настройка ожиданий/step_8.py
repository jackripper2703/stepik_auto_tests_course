# import time
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# link = "http://suninjuly.github.io/explicit_wait2.html"
# driver.get(link)
# driver.implicitly_wait(10)
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     text_price = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#price")))
#     text_book = driver.find_element(By.CSS_SELECTOR,"#book")
#
#     while text_price.text != "$100":
#         time.sleep(0.1)
#     else:
#         text_book.click()
#
#     input_value = driver.find_element(By.CSS_SELECTOR, "#input_value")
#     form_control = driver.find_element(By.CSS_SELECTOR,".form-control")
#     form_control.send_keys(calc(input_value.text))
#
#     submit = driver.find_element(By.CSS_SELECTOR, "#solve")
#     submit.click()
#
# finally:
#     time.sleep(10)
#     driver.quit()

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(LINK)

        # Ждем, пока цена станет $100
        price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

        # Нажимаем кнопку Book
        book_btn = driver.find_element(By.ID, "book")
        book_btn.click()

        # Решаем математическую задачу
        x_value = driver.find_element(By.ID, "input_value").text
        answer_input = driver.find_element(By.ID, "answer")
        answer_input.send_keys(calc(x_value))

        submit_btn = driver.find_element(By.ID, "solve")
        submit_btn.click()

finally:
    # Закрываем браузер в любом случае
    driver.quit()