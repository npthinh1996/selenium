from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import unittest
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(executable_path="webdriver/firefox", options=option)
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        # TODO: Enter username
        usrName = "..."
        # TODO: Enter password
        usrPass = "..."

        emailId = "email"
        passId = "pass"
        loginId = "loginbutton"
        
        emailField = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(emailId))
        passField = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(passId))
        loginBut = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(loginId))

        emailField.send_keys(usrName)
        passField.send_keys(usrPass)
        loginBut.click()

        WebDriverWait(driver, 5).until(lambda driver: driver.title == "Facebook")

        likeBut = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_link_text("Thích"))
        likeBut.click()

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
