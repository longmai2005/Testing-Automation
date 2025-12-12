from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestCase01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

        self.driver.get('http://railwayb1.somee.com/')

    def test_login(self):
        self.home_page.go_to_login_page()

        self.login_page.login('cijnuj@ramcloud.us', '123456789')

        self.assertEqual(self.home_page.get_welcome_msg(), 'Welcome cijnuj@ramcloud.us')

if __name__ == '__main__':
    unittest.main()