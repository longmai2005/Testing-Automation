import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

class HomeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_TC_HOME_01_ui_display(self):
        """TC_HOME_01: Kiểm tra giao diện trang Home"""
        print("\n--- TC_HOME_01 ---")
        self.assertIn("Safe Railway", self.driver.title)
        header = self.driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertIn("Welcome to Safe Railway", header)

    def test_TC_HOME_02_nav_guest(self):
        """TC_HOME_02: Điều hướng khi chưa đăng nhập"""
        print("\n--- TC_HOME_02 ---")
        self.home_page.go_to_contact_page()
        self.assertIn("contact", self.driver.find_element(By.CSS_SELECTOR, "h1").text.lower())
        
        self.home_page.go_to_timetable_page()
        self.assertIn("timetable", self.driver.find_element(By.CSS_SELECTOR, "h1").text.lower())
        
        self.home_page.go_to_book_ticket_page()
        self.assertIn("Login", self.driver.title)

    def test_TC_HOME_03_nav_user(self):
        """TC_HOME_03: Điều hướng khi đã đăng nhập"""
        print("\n--- TC_HOME_03 ---")
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789") 
        
        self.home_page.go_to_change_password_page()
        self.assertIn("change password", self.driver.find_element(By.CSS_SELECTOR, "h1").text.lower())
        
        self.home_page.go_to_book_ticket_page()
        self.assertIn("book ticket", self.driver.find_element(By.CSS_SELECTOR, "h1").text.lower())

    def test_TC_HOME_04_external_link(self):
        """TC_HOME_04: Kiểm tra liên kết ngoài"""
        print("\n--- TC_HOME_04 ---")
        self.home_page.go_to_contact_page()
        email_link = self.driver.find_element(By.CSS_SELECTOR, ".contact a").get_attribute("href")
        self.assertIn("mailto:", email_link)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()