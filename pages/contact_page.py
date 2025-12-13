from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_HEADER = (By.CSS_SELECTOR, '#content h1')
    EMAIL_INFO = (By.CSS_SELECTOR, 'div.contact a[href^="mailto"]')

    def get_header_text(self):
        return self.get_element_text(self.CONTACT_HEADER)