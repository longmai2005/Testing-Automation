import unittest
import sys
import os
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
        """Check UI elements"""
        print("\n--- TC_HOME_01: UI Display ---")
        self.assertIn("Safe Railway", self.driver.title)

    def test_TC_HOME_02_nav_not_logged_in(self):
        """Check navigation when NOT logged in"""
        print("\n--- TC_HOME_02: Navigation (Guest) ---")
        self.home_page.go_to_contact_page()
        self.assertIn("Contact", self.driver.title)
        
        self.home_page.go_to_timetable_page()
        self.assertIn("TrainTimeTable", self.driver.page_source)

    def test_TC_HOME_03_nav_logged_in(self):
        """Check navigation when LOGGED IN"""
        print("\n--- TC_HOME_03: Navigation (User) ---")

        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789") 
        
        self.home_page.go_to_change_password_page()
        self.assertIn("Change Password", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()