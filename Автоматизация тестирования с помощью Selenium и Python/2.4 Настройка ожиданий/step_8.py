import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(Service('/Users/dev/JACK RIPPER/chrome/chromedriver'))
wait = WebDriverWait(driver, 12)

LINK = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(LINK)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Ждем, пока цена станет $100
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем кнопку Book
    book_btn = driver.find_element(By.ID, "book")
    book_btn.click()

    # Решаем математическую задачу
    x_value = driver.find_element(By.ID, "input_value").text
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(calc(x_value))

    submit = driver.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()

finally:
    time.sleep(10)
    driver.quit()