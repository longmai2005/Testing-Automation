import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TicketPriceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)

    def test_TC_PRICE_01_ui(self):
        """TC_PRICE_01: UI Ticket Price displays properly"""
        print("\n--- TC_PRICE_01 ---")
        self.home_page.go_to_ticket_price_page()
        header = self.driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertIn("Ticket Price", header)
        
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table.MyTable tr")
        self.assertGreater(len(rows), 1, "Price table is empty")

    def test_TC_PRICE_02_check_price_logic(self):
        """TC_PRICE_02: Check price for specific trip"""
        self.home_page.go_to_ticket_price_page()
        prices = self.driver.find_elements(By.XPATH, "//table[@class='MyTable']//td[count(//th[text()='Price']/preceding-sibling::th)+1]")
        for price in prices:
            self.assertNotEqual(price.text, "", "Price should not be empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()