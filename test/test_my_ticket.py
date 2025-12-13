import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_ticket_page import MyTicketPage

class MyTicketTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.my_ticket_page = MyTicketPage(self.driver)
        
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")

    def test_TC_MYT_01_02_view_list(self):
        """TC_MYT_01 & 02: View list"""
        self.driver.find_element(By.LINK_TEXT, "My ticket").click()
        rows = self.my_ticket_page.get_all_rows()

        print(f"Tickets found: {len(rows)-1}")

    def test_TC_MYT_03_cancel(self):
        """TC_MYT_03: Hủy vé"""
        self.driver.find_element(By.LINK_TEXT, "My ticket").click()
        try:
            self.my_ticket_page.cancel_first_ticket()

        except:
            print("No ticket to cancel")

    def test_TC_MYT_05_07_filter(self):
        """TC_MYT_05 -> 07: Filter"""

        self.driver.find_element(By.LINK_TEXT, "My ticket").click()

        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()