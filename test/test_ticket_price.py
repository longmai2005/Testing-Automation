import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage

class TicketPriceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)

    def test_TC01_ticket_price_display(self):
        """Verify ticket price table headers"""
        print("\n--- TC01: Verify Ticket Price Table ---")
        self.home_page.go_to_ticket_price_page()
        
        table = self.driver.find_element(By.CSS_SELECTOR, "table.MyTable")
        self.assertTrue(table.is_displayed())
        
        header_text = table.find_element(By.CSS_SELECTOR, "tr.TableSmallHeader").text
        self.assertIn("Seat Type", header_text)
        self.assertIn("Price", header_text)

    def test_TC02_check_price_link(self):
        """Verify clicking 'Check Price' from Timetable redirects correctly"""

        pass 

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()