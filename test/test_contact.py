import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.contact_page import ContactPage

class ContactTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.contact_page = ContactPage(self.driver)

    def test_TC01_contact_info_correct(self):
        """Verify contact email is displayed correctly"""
        print("\n--- TC01: Verify Contact Info ---")
        self.home_page.go_to_contact_page()
        
        header = self.contact_page.get_header_text()
        self.assertIn("contact", header.lower())
        
        content = self.driver.find_element(By.CSS_SELECTOR, ".contact").text
        print(f"Contact Content: {content}")
        self.assertIn("@", content) 

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()