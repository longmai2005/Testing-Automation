import unittest
import time
import random
import string
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.book_ticket_page import BookTicketPage
from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By

class RailwayTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://railwayb1.somee.com/')
        
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.book_page = BookTicketPage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def generate_random_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"auto_{random_str}@gmail.com"

    def generate_random_pid(self):
        return ''.join(random.choices(string.digits, k=9)) 

    def test_full_flow(self):
        """TC_Full: Register -> Login -> Book Ticket"""
    
        email = self.generate_random_email()
        pid = self.generate_random_pid() 
        password = "Password123!"
        
        print(f"\n--- Testing with Account: {email} | PID: {pid} ---")

        print("Step 1: Go to Register Page")
        self.home_page.go_to_register_page()
        
        print("Step 2: Register account")
        self.register_page.register(email, password, pid)
        
        print("Step 3: Perform Login")
        self.home_page.go_to_login_page()
        self.login_page.login(email, password)

        welcome_text = self.home_page.get_welcome_msg()
        print(f"Login Status: {welcome_text}")
        self.assertIn(email, welcome_text)

        print("Step 4: Go to Book Ticket Page")
        self.home_page.go_to_book_ticket_page()

        print("Step 5: Book a ticket")
        try:
            self.book_page.book_ticket(
                depart='Đà Nẵng',
                arrive='Huế',
                seat='Soft seat',
                amount='1'
            )
            
            print("Step 6: Verify Booking Success")
            
            success_header = self.driver.find_element(By.CSS_SELECTOR, "h1")
            actual_text = success_header.text
            
            print(f"Result Page Header: {actual_text}")
            
            self.assertIn("ticket booked successfully!", actual_text.lower(), "Booking Failed: Success message not found!")
            
            print(">>> TEST PASSED: Quy trình đặt vé hoàn tất chính xác!")
            
        except Exception as e:
            self.driver.save_screenshot('error_booking.png')
            self.fail(f"Booking failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()