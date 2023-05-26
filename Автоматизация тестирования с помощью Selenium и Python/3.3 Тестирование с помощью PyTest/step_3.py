from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPeps:
    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def step(self, link):
        self.browser.get(link)
        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Gordon")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Freeman")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("gordon@freem.an")
        button = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_step_10(self):
        self.setup_method()
        a = self.step("https://suninjuly.github.io/registration1.html")
        assert "Congratulations! You have successfully registered!" == a


    def test_step_11(self):
        self.setup_method()
        a = self.step("https://suninjuly.github.io/registration2.html")
        assert "Congratulations! You have successfully registered!" == a



if __name__ == "__main__":
    test_peps = TestPeps()
    test_peps.test_step_10()
    test_peps.test_step_11()
