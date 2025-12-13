import unittest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('http://railwayb1.somee.com/')
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_TC_LOG_03_non_existing_email(self):
        """Login with non-existing email"""
        print("\n--- TC_LOG_03: Non-existing Email ---")
        self.home_page.go_to_login_page()
        self.login_page.login("khongtontai@gmail.com", "123456")
        
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        self.assertIn("username or password", error.lower())

    def test_TC_LOG_09_password_masked(self):
        """Verify password field is masked"""
        print("\n--- TC_LOG_09: Password Masked ---")
        self.home_page.go_to_login_page()
        pass_field = self.driver.find_element(By.ID, "password")
        field_type = pass_field.get_attribute("type")
        self.assertEqual(field_type, "password", "Password field is NOT masked!")

    def test_TC_LOG_10_lock_account(self):
        """Login incorrectly 5 times triggers lock"""
        print("\n--- TC_LOG_10: Account Lockout ---")
        self.home_page.go_to_login_page()
        
        for i in range(5):
            self.login_page.login("testlock@gmail.com", "wrongpass")
            self.driver.refresh() 
        
        self.login_page.login("testlock@gmail.com", "wrongpass")
        error = self.driver.find_element(By.CSS_SELECTOR, "p.message.error").text
        print(f"Lock Msg: {error}")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()