from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):

    TAB_LOGIN = (By.LINK_TEXT, 'Login')
    TAB_REGISTER = (By.LINK_TEXT, 'Register')
    TAB_BOOK_TICKET = (By.LINK_TEXT, 'Book ticket')
    WELCOME_MSG = (By.CSS_SELECTOR, 'div.account strong')

    def go_to_login_page(self):
        self.do_click(self.TAB_LOGIN)

    def go_to_register_page(self):
        self.do_click(self.TAB_REGISTER)

    def go_to_book_ticket_page(self):
        self.do_click(self.TAB_BOOK_TICKET)

    def get_welcome_msg(self) -> str:
        return self.get_element_text(self.WELCOME_MSG)