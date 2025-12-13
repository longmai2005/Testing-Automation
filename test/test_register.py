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

    def test_TC_REG_01_ui(self):
        """TC_REG_01: Kiểm tra UI trang Register"""
        self.home_page.go_to_register_page()
        self.assertIn("Register", self.driver.title)

        tab_class = self.driver.find_element(By.css_selector, "li.selected a").text
        self.assertEqual(tab_class, "Register")

    def test_TC_REG_02_success(self):
        """TC_REG_02: Đăng ký thành công"""
        self.home_page.go_to_register_page()
        self.register_page.register(self.generate_email(), "Pass123!", "123456789")

    def test_TC_REG_03_email_exists(self):
        """TC_REG_03: Email đã tồn tại"""
        self.home_page.go_to_register_page()
        self.register_page.register("cijnuj@ramcloud.us", "123456789", "123456789")
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("exists", error.lower())

    def test_TC_REG_04_05_invalid_email(self):
        """TC_REG_04 & 05: Email sai độ dài hoặc định dạng"""
        self.home_page.go_to_register_page()
        self.register_page.register("invalid", "Pass123!", "123456789")

    def test_TC_REG_06_pass_mismatch(self):
        """TC_REG_06: Password không khớp"""
        self.home_page.go_to_register_page()
        self.register_page.register(self.generate_email(), "PassA", "PassB", "123456789") 
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("confirm password", error.lower())

    def test_TC_REG_07_08_invalid_pass(self):
        """TC_REG_07 & 08: Password sai độ dài hoặc ký tự"""
        self.home_page.go_to_register_page()
        self.register_page.register(self.generate_email(), "1", "123456789") 
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("password", error.lower())

    def test_TC_REG_09_masked_pass(self):
        """TC_REG_09: Password được che"""
        self.home_page.go_to_register_page()
        attr = self.driver.find_element(By.ID, "password").get_attribute("type")
        self.assertEqual(attr, "password")

    def test_TC_REG_10_11_invalid_pid(self):
        """TC_REG_10 & 11: PID sai"""
        self.home_page.go_to_register_page()
        self.register_page.register(self.generate_email(), "Pass123!", "abc")
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("id", error.lower())

    def test_TC_REG_12_nav_link(self):
        """TC_REG_12: Link login here"""
        self.home_page.go_to_register_page()
        self.driver.find_element(By.LINK_TEXT, "Login page").click() 
        self.assertIn("Login", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()