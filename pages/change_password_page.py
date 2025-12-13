from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ChangePasswordPage(BasePage):
    CURRENT_PASSWORD_TXT = (By.ID, 'currentPassword')
    NEW_PASSWORD_TXT = (By.ID, 'newPassword')
    CONFIRM_PASSWORD_TXT = (By.ID, 'confirmPassword')
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, 'input[value="Change Password"]')
    
    SUCCESS_MSG = (By.CSS_SELECTOR, 'p.message.success')

    def change_password(self, current_pass, new_pass):
        self.do_send_keys(self.CURRENT_PASSWORD_TXT, current_pass)
        self.do_send_keys(self.NEW_PASSWORD_TXT, new_pass)
        self.do_send_keys(self.CONFIRM_PASSWORD_TXT, new_pass)
        
        self.scroll_into_view(self.CHANGE_PASSWORD_BTN)
        self.do_click(self.CHANGE_PASSWORD_BTN)

    def get_success_msg(self):
        return self.get_element_text(self.SUCCESS_MSG)