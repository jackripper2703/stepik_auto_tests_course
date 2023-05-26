import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '/Users/dev/JACK RIPPER/chrome/chromedriver'
service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

class Test_uni(unittest.TestCase):
    LINK = "http://suninjuly.github.io/registration1.html"

    def step_11(self, link):
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Gordon")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Freeman")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("gordon@freem.an")
        button = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        return welcome_text


    def test_step_10(self):
        a = self.step_11("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!" == a, True)

    def test_step_11(self):
        a = self.step_11("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!" == a, True)
        browser.close()

if __name__ == "__main__":
    unittest.main()
