from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL_TXT_LOCATOR = (By.ID, 'username')
    PASSWORD_TXT_LOCATOR = (By.NAME, 'password')
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, 'input[value=login]')

    # Constructor
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Actions
    def enter_email(self, email: str):
        self.driver.find_element(*self.EMAIL_TXT_LOCATOR).send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_TXT_LOCATOR).send_keys(password)

    def click_login_btn(self):
        login_btn = self.driver.find_element(*self.LOGIN_BTN_LOCATOR)
        # Scroll this element into view before click it
        self.driver.execute_script('arguments[0].scrollIntoView();', login_btn)
        login_btn.click()

        # Waiting for the page to load after clicking the login button
        # Wait for the login_btn is disappear (or not display or invisibility)
        driver_wait = WebDriverWait(self.driver, timeout=10)
        driver_wait.until(EC.invisibility_of_element(login_btn))

    def login(self, username: str, password: str):
        self.enter_email(username)
        # 
        self.enter_password(password)
        self.click_login_btn()