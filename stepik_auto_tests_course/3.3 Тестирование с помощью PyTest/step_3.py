class TestTEXT:

    def test_1(self, driver, register):
        driver.get("https://suninjuly.github.io/registration1.html")
        a = register
        assert "Congratulations! You have successfully registered!" == a


    def test_2(self, driver, register):
        driver.get("https://suninjuly.github.io/registration2.html")
        a = register
        assert "Congratulations! You have successfully registered!" == a
