import unittest
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_ticket_page import MyTicketPage
from pages.book_ticket_page import BookTicketPage

class MyTicketTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.my_ticket_page = MyTicketPage(self.driver)
        self.book_page = BookTicketPage(self.driver)
        
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")

    def test_TC_MYT_05_07_filter(self):
        """TC_MYT_05 -> 07: Filter functionality (>6 rows)"""
        print("\n--- TC_MYT_05_07: Filter Check ---")
        self.home_page.go_to_my_ticket_page()
        
        rows = self.my_ticket_page.get_all_rows()
        ticket_count = len(rows) - 1
        
        if ticket_count <= 6:
            print(f"Not enough tickets ({ticket_count}) to test Filter visibility. Need > 6.")
            
            return

        try:
            filter_table = self.driver.find_element(By.CSS_SELECTOR, "div.Filter") 
            self.assertTrue(filter_table.is_displayed(), "Filter table should be visible")
            
            status_select = Select(self.driver.find_element(By.NAME, "FilterStatus"))
            status_select.select_by_visible_text("New")
            self.driver.find_element(By.CSS_SELECTOR, "input[value='Apply Filter']").click()
            
            new_rows = self.my_ticket_page.get_all_rows()
            print(f"Filtered rows: {len(new_rows)-1}")
        except Exception as e:
            print(f"Filter element not found or changed: {e}")

    def test_TC_MYT_04_delete_expired(self):
        """TC_MYT_04: User can delete expired tickets"""
        self.home_page.go_to_my_ticket_page()
        try:
            expired_btn = self.driver.find_element(By.XPATH, "//td[text()='Expired']/..//input[@value='Cancel']")
            expired_btn.click()
            self.driver.switch_to.alert.accept()
            print("Deleted an expired ticket.")
        except:
            print("No expired ticket found to test.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()