import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.feature("Module: Register")
class TestRegister:

    def fill_form(self, driver, email, password, confirm_pass, pid):
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "confirmPassword").send_keys(confirm_pass)
        driver.find_element(By.ID, "pid").send_keys(pid)
        
        btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(0.5)
        btn.click()

    @allure.story("TC_REG_02: Đăng ký thành công (Valid Data)")
    def test_register_success(self, driver, base_url):
        driver.get(f"{base_url}/Account/Register.cshtml")
        email = f"auto_{int(time.time())}@ramcloud.us"
        
        with allure.step(f"Đăng ký với email: {email}"):
            self.fill_form(driver, email, "12345678", "12345678", "123456789")
            
        assert "Welcome" in driver.page_source or "Login" in driver.current_url

    @allure.story("TC_REG_05 & 08: Đăng ký thất bại - Email không hợp lệ")
    @pytest.mark.parametrize("invalid_email", [
        "missing_at_gmail.com",   
        "chau1234@",              
        "a@b",                    
        "a" * 33 + "@gmail.com"   
    ])
    def test_register_invalid_email(self, driver, base_url, invalid_email):
        driver.get(f"{base_url}/Account/Register.cshtml")
        self.fill_form(driver, invalid_email, "12345678", "12345678", "123456789")
        
        assert len(driver.find_elements(By.CLASS_NAME, "validation-summary-errors")) > 0 or \
               len(driver.find_elements(By.CLASS_NAME, "field-validation-error")) > 0

    @allure.story("TC_REG_06: Password và Confirm Password không khớp")
    def test_register_pass_mismatch(self, driver, base_url):
        driver.get(f"{base_url}/Account/Register.cshtml")
        self.fill_form(driver, "valid@email.com", "12345678", "87654321", "123456789")
        
        err = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        assert "password and confirmation password do not match" in err

    @allure.story("TC_REG_10 & 11: Invalid PID (Độ dài & Format)")
    @pytest.mark.parametrize("invalid_pid", [
        "123",             
        "1" * 21,          
        "abc123456",        
        "@#$123456"         
    ])
    def test_register_invalid_pid(self, driver, base_url, invalid_pid):
        driver.get(f"{base_url}/Account/Register.cshtml")
        self.fill_form(driver, "valid@email.com", "12345678", "12345678", invalid_pid)
        
        err = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        assert "ID length" in err or "ID format" in err or "valid" in err

    @allure.story("TC_REG_09: Kiểm tra Password Masked (Che dấu)")
    def test_password_masked(self, driver, base_url):
        driver.get(f"{base_url}/Account/Register.cshtml")
        pass_field = driver.find_element(By.ID, "password")
        assert pass_field.get_attribute("type") == "password", "Password không được che!"