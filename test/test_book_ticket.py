import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.book_ticket_page import BookTicketPage

class BookTicketTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.book_page = BookTicketPage(self.driver)

    def test_TC_BOOK_01_redirect(self):
        """Redirect to Login if not logged in"""
        print("\n--- TC_BOOK_01: Redirect Check ---")
        self.home_page.go_to_book_ticket_page()

        self.assertIn("Login", self.driver.title)

    def test_TC_BOOK_06_book_success(self):
        """Book ticket successfully"""
        print("\n--- TC_BOOK_06: Book Success ---")
    
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789") 

        self.home_page.go_to_book_ticket_page()
        self.book_page.book_ticket("Đà Nẵng", "Huế", "Soft seat", "1")
        
        self.assertIn("ticket booked successfully", self.driver.page_source.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()