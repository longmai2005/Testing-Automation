import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.ticket_price_page import TicketPricePage

class TicketPriceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.price_page = TicketPricePage(self.driver)

    def test_TC_PRICE_01_03_ui_data(self):
        """TC_PRICE_01 -> 03: UI & Data"""
        self.home_page.go_to_ticket_price_page()

    def test_TC_PRICE_04_book_guest(self):
        """TC_PRICE_04: Book (Guest)"""

        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()