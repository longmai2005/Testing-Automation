from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_TXT = (By.ID, 'username')
    PASSWORD_TXT = (By.ID, 'password') 
    LOGIN_BTN = (By.CSS_SELECTOR, 'input[value=login]')

    def login(self, username, password):
        self.do_send_keys(self.EMAIL_TXT, username)
        self.do_send_keys(self.PASSWORD_TXT, password)
        self.scroll_into_view(self.LOGIN_BTN)
        self.do_click(self.LOGIN_BTN)