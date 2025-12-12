from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:

    NAV_BAR_LOGIN_LOCATOR = (By.LINK_TEXT, 'Login')
    WELCOME_MSG_LOCATOR = (By.CSS_SELECTOR, 'div.account strong')

    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver

    def go_to_login_page(self):
        self.driver.find_element(*self.NAV_BAR_LOGIN_LOCATOR).click()

    def get_welcome_msg(self) -> str:
        return self.driver.find_element(*self.WELCOME_MSG_LOCATOR).text