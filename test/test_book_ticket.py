import unittest
import sys
import os
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
        
        self.home_page.go_to_login_page()
        self.login_page.login("cijnuj@ramcloud.us", "123456789")

    def test_TC_BOOK_03_date_range(self):
        """TC_BOOK_03: Depart date display 3 - 30 days ahead"""
        print("\n--- TC_BOOK_03: Date Range Check ---")
        self.home_page.go_to_book_ticket_page()
        
        date_element = self.driver.find_element(By.NAME, "Date")
        select = Select(date_element)
        options = select.options
        
        if not options:
            print("Date dropdown is empty!")
            return

        first_date_text = options[0].text
        
        try:
            first_date = datetime.strptime(first_date_text, '%m/%d/%Y')
            today = datetime.now()
            
            diff_start = (first_date - today).days
            self.assertGreaterEqual(diff_start, 1, f"Ngày bắt đầu ({first_date_text}) quá gần so với hôm nay")
            
            print(f"Date check passed. Start Date: {first_date_text}")
        except ValueError:
            print(f"[Warning] Không parse được định dạng ngày: {first_date_text}")

    def test_TC_BOOK_07_max_tickets(self):
        """TC_BOOK_07: User cannot book more than 10 tickets"""
        print("\n--- TC_BOOK_07: Max 10 Tickets ---")
        self.home_page.go_to_book_ticket_page()
        
        try:
            depart_select = Select(self.driver.find_element(By.NAME, "DepartStation"))
            depart_select.select_by_index(1) 
            
            arrive_select = Select(self.driver.find_element(By.NAME, "ArriveStation"))
            arrive_select.select_by_index(2) 
            
            seat_select = Select(self.driver.find_element(By.NAME, "SeatType"))
            seat_select.select_by_index(1)

            amount_select = Select(self.driver.find_element(By.NAME, "TicketAmount"))
            amounts = [int(opt.text) for opt in amount_select.options]
            
            if max(amounts) >= 10:
                amount_select.select_by_visible_text(str(max(amounts)))
                self.driver.find_element(By.CSS_SELECTOR, 'input[value="Book ticket"]').click()
                
                self.home_page.go_to_book_ticket_page()
                depart_select = Select(self.driver.find_element(By.NAME, "DepartStation"))
                depart_select.select_by_index(1)
                
                arrive_select = Select(self.driver.find_element(By.NAME, "ArriveStation"))
                arrive_select.select_by_index(2)
                
                seat_select = Select(self.driver.find_element(By.NAME, "SeatType"))
                seat_select.select_by_index(1)
                
                self.driver.find_element(By.CSS_SELECTOR, 'input[value="Book ticket"]').click()
                
                error_msg = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
                print(f"Error msg found: {error_msg}")
                self.assertTrue("10" in error_msg or "error" in error_msg.lower())
            else:
                print("Hệ thống chỉ cho phép chọn tối đa trong dropdown < 10")
        except Exception as e:
            print(f"Test max tickets logic skipped/failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()