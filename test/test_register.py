import unittest
import sys
import os
import random
import string
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.register_page import RegisterPage

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def generate_email(self):
        return f"auto_{''.join(random.choices(string.ascii_lowercase, k=8))}@gmail.com"

    def test_TC_REG_02_success(self):
        """Register valid info"""
        print("\n--- TC_REG_02: Register Success ---")
        self.home_page.go_to_register_page()
        self.register_page.register(self.generate_email(), "Pass123!", "123456789")

    def test_TC_REG_06_password_mismatch(self):
        """Error when confirm password mismatch"""
        print("\n--- TC_REG_06: Password Mismatch ---")
        self.home_page.go_to_register_page()
        
        self.driver.find_element(By.ID, "email").send_keys(self.generate_email())
        self.driver.find_element(By.ID, "password").send_keys("Pass123")
        self.driver.find_element(By.ID, "confirmPassword").send_keys("Pass456") # Sai
        self.driver.find_element(By.ID, "pid").send_keys("123456789")
        self.driver.find_element(By.CSS_SELECTOR, "input[value=Register]").click()
        
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        print(f"Error: {error}")
        self.assertIn("confirm password", error.lower())

    def test_TC_REG_10_invalid_pid(self):
        """Error when PID length is invalid"""
        print("\n--- TC_REG_10: Invalid PID Length ---")
        self.home_page.go_to_register_page()
        self.register_page.register(self.generate_email(), "Pass123!", "123") # PID quá ngắn
        
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("length", error.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()