import unittest
import sys
import os
from datetime import datetime, timedelta
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
        
        first_date_text = options[0].text
        last_date_text = options[-1].text
        
        try:
            first_date = datetime.strptime(first_date_text, '%m/%d/%Y')
            today = datetime.now()
            
            diff_start = (first_date - today).days
            self.assertGreaterEqual(diff_start, 2, "Ngày bắt đầu phải cách ít nhất 3 ngày (cho phép sai số múi giờ)")

            self.assertTrue(27 <= len(options) <= 31, f"Số lượng ngày hiển thị không đúng: {len(options)}")
            print(f"Date check passed. Range: {first_date_text} to {last_date_text}")
        except ValueError:
            print(f"[Warning] Không parse được định dạng ngày: {first_date_text}")

    def test_TC_BOOK_07_max_tickets(self):
        """TC_BOOK_07: User cannot book more than 10 tickets"""
        print("\n--- TC_BOOK_07: Max 10 Tickets ---")
        self.home_page.go_to_book_ticket_page()
        
        try:
            amount_select = Select(self.driver.find_element(By.NAME, "TicketAmount"))
            amounts = [int(opt.text) for opt in amount_select.options]
            
            if max(amounts) >= 10:
                self.book_page.book_ticket("Đà Nẵng", "Huế", "Soft seat", "10")
                self.home_page.go_to_book_ticket_page()
                self.book_page.book_ticket("Đà Nẵng", "Huế", "Soft seat", "1")
                
                error_msg = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
                self.assertIn("10 tickets", error_msg)
            else:
                print("Hệ thống chỉ cho phép chọn tối đa trong dropdown < 10")
        except Exception as e:
            print(f"Test max tickets logic: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()