import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.timetable_page import TimetablePage

class TimetableTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.timetable_page = TimetablePage(self.driver)

    def test_TC01_timetable_display(self):
        """Verify timetable page loads correctly"""
        print("\n--- TC01: Verify Timetable Page Display ---")
        self.home_page.go_to_timetable_page()
        
        header = self.driver.find_element_by_tag_name('h1').text
        self.assertIn("train timetable", header.lower())

    def test_TC02_check_specific_route(self):
        """Verify route 'Đà Nẵng to Sài Gòn' exists"""
        print("\n--- TC02: Verify Route Da Nang - Sai Gon exists ---")
        self.home_page.go_to_timetable_page()
        
        exists = self.timetable_page.check_train_exist("Đà Nẵng", "Sài Gòn")
        print(f"Route Found: {exists}")
        self.assertTrue(exists, "Route from Da Nang to Sai Gon not found!")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()