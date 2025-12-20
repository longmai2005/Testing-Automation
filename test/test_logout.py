import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

class LogoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")

    def test_TC_LOGOUT_01_ui(self):
        """TC_LOGOUT_01: Logout control is visible"""
        print("\n--- TC_LOGOUT_01 ---")
        logout_tab = self.driver.find_element(By.CSS_SELECTOR, "a[href='/Account/Logout']")
        self.assertTrue(logout_tab.is_displayed())

    def test_TC_LOGOUT_02_success(self):
        """TC_LOGOUT_02: User can log out successfully"""
        print("\n--- TC_LOGOUT_02 ---")
        self.home_page.logout()
        
        self.assertNotIn("Logout", self.driver.page_source)
        self.assertIn("Login", self.driver.page_source) 
        
        self.home_page.go_to_my_ticket_page()
        self.assertIn("Login", self.driver.title, "Should redirect to Login page")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()