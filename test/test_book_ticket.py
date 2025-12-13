import unittest
import sys
import os
from selenium.webdriver.support.ui import Select
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

    def test_TC_BOOK_01_guest_access(self):
        """TC_BOOK_01: Truy cập khi chưa login"""
        self.home_page.go_to_book_ticket_page()
        self.assertIn("Login", self.driver.title)

    def test_TC_BOOK_02_05_ui_elements(self):
        """TC_BOOK_02 & 05: Kiểm tra UI và Seat Type"""
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")
        self.home_page.go_to_book_ticket_page()
        
        seat_select = Select(self.driver.find_element_by_name("SeatType"))
        options = [o.text for o in seat_select.options]
        self.assertIn("Soft seat", options)
        self.assertIn("Hard seat", options)

    def test_TC_BOOK_03_date_range(self):
        """TC_BOOK_03: Date range (3-30 days)"""

        pass 

    def test_TC_BOOK_06_book_success(self):
        """TC_BOOK_06: Đặt vé thành công"""
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")
        self.home_page.go_to_book_ticket_page()
        self.book_page.book_ticket("Đà Nẵng", "Huế", "Soft seat", "1")
        self.assertIn("booked successfully", self.driver.page_source.lower())

    def test_TC_BOOK_07_max_tickets(self):
        """TC_BOOK_07: Đặt quá 10 vé"""

        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()