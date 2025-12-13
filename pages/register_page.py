from selenium.webdriver.common.by import By
from base.base_page import BasePage

class RegisterPage(BasePage):
    EMAIL_TXT = (By.ID, 'email')
    PASSWORD_TXT = (By.ID, 'password')
    CONFIRM_PASSWORD_TXT = (By.ID, 'confirmPassword')
    PID_TXT = (By.ID, 'pid')
    REGISTER_BTN = (By.CSS_SELECTOR, 'input[value=Register]')
    
    SUCCESS_MSG = (By.CSS_SELECTOR, "#content h1") 

    ERROR_MSG = (By.CSS_SELECTOR, "p.message.error")

    def register(self, email, password, pid):
        self.do_send_keys(self.EMAIL_TXT, email)
        self.do_send_keys(self.PASSWORD_TXT, password)
        self.do_send_keys(self.CONFIRM_PASSWORD_TXT, password)
        self.do_send_keys(self.PID_TXT, pid)
        self.scroll_into_view(self.REGISTER_BTN)
        self.do_click(self.REGISTER_BTN)

    def verify_registration_success(self):
        try:
            element = self.wait.until(lambda d: d.find_element(*self.SUCCESS_MSG))
            return True
        except:
            return False