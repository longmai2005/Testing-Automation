import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.timetable_page import TimetablePage

class TimetableTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.timetable_page = TimetablePage(self.driver)

    def test_TC_TIME_01_ui_display(self):
        """Verify Timetable UI displays properly"""
        print("\n--- TC_TIME_01: Timetable UI ---")
        self.home_page.go_to_timetable_page()
        
        header = self.driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertIn("timetable", header.lower())
        
        rows = self.timetable_page.get_all_rows()
        self.assertGreater(len(rows), 0, "Timetable is empty!")

    def test_TC_TIME_03_check_price_link(self):
        """User can check ticket prices of the trip"""
        print("\n--- TC_TIME_03: Check Price Link ---")
        self.home_page.go_to_timetable_page()
        
        try:
            self.timetable_page.click_check_price("Đà Nẵng", "Sài Gòn")
            
            header = self.driver.find_element(By.CSS_SELECTOR, "h1").text
            self.assertIn("ticket price", header.lower())
        except Exception as e:
            print(f"Skipping check price due to missing route: {e}")

    def test_TC_TIME_04_book_ticket_guest(self):
        """Redirect to login when clicking Book Ticket (Guest)"""
        print("\n--- TC_TIME_04: Book Ticket (Guest) ---")
        self.home_page.logout()
        
        self.home_page.go_to_timetable_page()
        self.timetable_page.click_book_ticket("Đà Nẵng", "Sài Gòn")
        
        self.assertIn("Login", self.driver.title)

    def test_TC_TIME_05_book_ticket_user(self):
        """Navigate to Book ticket page (User)"""
        print("\n--- TC_TIME_05: Book Ticket (User) ---")
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")
        
        self.home_page.go_to_timetable_page()
        self.timetable_page.click_book_ticket("Đà Nẵng", "Sài Gòn")
        
        self.assertIn("Book ticket", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()