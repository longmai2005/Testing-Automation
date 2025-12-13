import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_TC_LOG_01_ui(self):
        """TC_LOG_01: UI Login"""
        self.home_page.go_to_login_page()
        self.assertIn("Login", self.driver.title)

    def test_TC_LOG_02_success(self):
        """TC_LOG_02: Login thành công"""
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")
        self.assertIn("Welcome", self.home_page.get_welcome_msg())

    def test_TC_LOG_03_06_invalid_credentials(self):
        """TC_LOG_03 & 06: Sai email hoặc pass"""
        self.home_page.go_to_login_page()
        self.login_page.login("wrong@mail.com", "wrongpass")
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("username or password", error.lower())

    def test_TC_LOG_05_08_html_injection(self):
        """TC_LOG_05 & 08: HTML Script injection"""
        self.home_page.go_to_login_page()
        self.login_page.login("<script>alert('xss')</script>", "pass")
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.fail("Security Vulnerability: Alert displayed!")
        except:
            pass 

    def test_TC_LOG_10_lockout(self):
        """TC_LOG_10: Khóa tài khoản sau 5 lần sai"""
        self.home_page.go_to_login_page()

        test_email = "lockme@test.com"
        for _ in range(6):
            self.login_page.login(test_email, "wrong")
            self.driver.refresh()
        
        self.login_page.login(test_email, "wrong")
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()