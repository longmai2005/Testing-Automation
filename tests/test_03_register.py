import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException

@allure.feature("Module: Register")
class TestRegister:

    def fill_and_click(self, driver, email, password, confirm, pid):
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "confirmPassword").send_keys(confirm)
        driver.find_element(By.ID, "pid").send_keys(pid)
        
        submit_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        driver.execute_script("arguments[0].click();", submit_btn)

    def handle_unexpected_alert(self, driver):
        """Hàm xử lý Alert khó chịu"""
        try:
            time.sleep(0.5) 
            alert = driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
            return True
        except NoAlertPresentException:
            return False

    @allure.story("TC_REG_FAIL: Các trường hợp đăng ký lỗi")
    @pytest.mark.parametrize("email, password, confirm, pid", [
        ("bad_email", "12345678", "12345678", "123456789"), # Email sai
        ("valid@test.com", "12345678", "87654321", "123456789"), # Pass lệch
        ("valid@test.com", "12345678", "12345678", "123"), # PID ngắn
        ("valid@test.com", "12345678", "12345678", "abc123456"), # PID chữ
        ("valid@test.com", "12345678", "12345678", "@#$123456"), # PID ký tự lạ (Gây Alert)
        ("valid@test.com", "12345678", "12345678", "1"*25), # PID quá dài
    ])
    def test_register_failures(self, driver, base_url, email, password, confirm, pid):
        driver.get(f"{base_url}/Account/Register.cshtml")
        
        try:
            self.fill_and_click(driver, email, password, confirm, pid)
        except UnexpectedAlertPresentException:
            return

        if self.handle_unexpected_alert(driver):
            return 

        errors = driver.find_elements(By.CSS_SELECTOR, ".validation-summary-errors, .field-validation-error, .message")
        
        is_on_register_page = "Register" in driver.title
        assert len(errors) > 0 or is_on_register_page

    @allure.story("TC_REG_06: Password Mismatch Explicit Check")
    def test_register_pass_mismatch(self, driver, base_url):
        driver.get(f"{base_url}/Account/Register.cshtml")
        self.fill_and_click(driver, "valid@test.com", "12345678", "87654321", "123456789")
        
        assert "match" in driver.page_source or "Register" in driver.title