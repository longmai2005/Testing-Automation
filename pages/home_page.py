from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    # Locators
    TAB_LOGIN = (By.LINK_TEXT, 'Login')
    TAB_REGISTER = (By.LINK_TEXT, 'Register')
    TAB_BOOK_TICKET = (By.LINK_TEXT, 'Book ticket')
    WELCOME_MSG = (By.CSS_SELECTOR, 'div.account strong')
    
    TAB_CONTACT = (By.LINK_TEXT, 'Contact')
    TAB_TIMETABLE = (By.LINK_TEXT, 'Timetable')
    TAB_TICKET_PRICE = (By.LINK_TEXT, 'Ticket price')
    TAB_CHANGE_PASSWORD = (By.LINK_TEXT, 'Change password')
    TAB_LOGOUT = (By.LINK_TEXT, 'Log out')

    def go_to_login_page(self):
        self.do_click(self.TAB_LOGIN)

    def go_to_register_page(self):
        self.do_click(self.TAB_REGISTER)

    def go_to_book_ticket_page(self):
        self.do_click(self.TAB_BOOK_TICKET)

    def get_welcome_msg(self) -> str:
        return self.get_element_text(self.WELCOME_MSG)

    def go_to_contact_page(self):
        self.do_click(self.TAB_CONTACT)

    def go_to_timetable_page(self):
        self.do_click(self.TAB_TIMETABLE)

    def go_to_ticket_price_page(self):
        self.do_click(self.TAB_TICKET_PRICE)

    def go_to_change_password_page(self):
        self.do_click(self.TAB_CHANGE_PASSWORD)

    def logout(self):
        self.do_click(self.TAB_LOGOUT)