import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.book_ticket_page import BookTicketPage
from pages.my_ticket_page import MyTicketPage

class MyTicketTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.book_page = BookTicketPage(self.driver)
        self.my_ticket_page = MyTicketPage(self.driver)

        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")

    def test_TC_MYT_02_view_ticket(self):
        """View booked tickets"""
        print("\n--- TC_MYT_02: View Ticket ---")

        self.home_page.go_to_book_ticket_page()
        self.book_page.book_ticket("Sài Gòn", "Nha Trang", "Soft seat", "1")

        self.driver.find_element(By.LINK_TEXT, "My ticket").click()
        
        exists = self.my_ticket_page.is_ticket_displayed("Sài Gòn", "Nha Trang")
        self.assertTrue(exists, "Booked ticket not found in My Ticket!")

    def test_TC_MYT_03_cancel_ticket(self):
        """Cancel a ticket"""
        print("\n--- TC_MYT_03: Cancel Ticket ---")
        self.driver.find_element(By.LINK_TEXT, "My ticket").click()
        
        rows_before = len(self.my_ticket_page.get_all_rows())
        
        if rows_before > 1: 
            self.my_ticket_page.cancel_first_ticket()

            rows_after = len(self.my_ticket_page.get_all_rows())
            self.assertEqual(rows_after, rows_before - 1, "Ticket count mismatch after cancel")
        else:
            print("No ticket to cancel")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()