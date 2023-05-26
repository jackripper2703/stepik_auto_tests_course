import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '/Users/dev/JACK RIPPER/chrome/chromedriver'
service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

LINK = "http://suninjuly.github.io/registration1.html"
browser.get(LINK)
try:
    # Заполнение обязательных полей
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Gordon")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Freeman")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("gordon@freem.an")

    # Отправка заполненной формы
    button = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()