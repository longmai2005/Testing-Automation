import unittest
import sys
import os
import random
import string
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.change_password_page import ChangePasswordPage

class ChangePasswordTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.cp_page = ChangePasswordPage(self.driver)
        
        self.email = f"auto_{''.join(random.choices(string.ascii_lowercase, k=8))}@gmail.com"
        self.password = "Pass123!"
        self.pid = ''.join(random.choices(string.digits, k=9))
        
        self.home_page.go_to_register_page()
        self.register_page.register(self.email, self.password, self.pid)
        self.home_page.go_to_login_page()
        self.login_page.login(self.email, self.password)

    def test_TC_CP_03_wrong_current_pass(self):
        """Change pass with WRONG current password"""
        print("\n--- TC_CP_03: Wrong Current Pass ---")
        self.home_page.go_to_change_password_page()
        self.cp_page.change_password("WrongPass", "NewPass123!")
        
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("password is incorrect", error.lower())

    def test_TC_CP_04_confirm_mismatch(self):
        """Change pass with Confirm Mismatch"""
        print("\n--- TC_CP_04: Confirm Mismatch ---")
        self.home_page.go_to_change_password_page()
        
        self.driver.find_element(By.ID, "currentPassword").send_keys(self.password)
        self.driver.find_element(By.ID, "newPassword").send_keys("NewPass123")
        self.driver.find_element(By.ID, "confirmPassword").send_keys("NewPass999")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Change Password']").click()
        
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("confirm password", error.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()