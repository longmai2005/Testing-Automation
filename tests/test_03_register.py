import pytest
import allure
from selenium.webdriver.common.by import By

@allure.feature("Module 2: Register")
class TestRegister:
    
    def open_register(self, driver):
        # Mở trang register
        driver.get("http://www.raillog.net/Account/Register.cshtml")

    @allure.story("TC_REG_02: Đăng ký thành công")
    def test_register_success(self, driver):
        self.open_register(driver)
        import time
        email = f"auto_{int(time.time())}@gmail.com" # Tạo email ngẫu nhiên để không trùng
        
        with allure.step("Nhập thông tin hợp lệ"):
            driver.find_element(By.ID, "email").send_keys(email)
            driver.find_element(By.ID, "password").send_keys("12345678")
            driver.find_element(By.ID, "confirmPassword").send_keys("12345678")
            driver.find_element(By.ID, "pid").send_keys("123456789")
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        
        with allure.step("Verify thành công"):
            # Kiểm tra thông báo hoặc chuyển trang
            assert driver.find_element(By.CLASS_NAME, "success-msg").is_displayed()

    @allure.story("TC_REG_06: Password và Confirm không khớp")
    def test_register_pass_mismatch(self, driver):
        self.open_register(driver)
        driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.ID, "confirmPassword").send_keys("654321")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        
        err = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        assert "password and confirmation password do not match" in err

    @allure.story("TC_REG_10: PID độ dài không hợp lệ")
    def test_register_pid_length(self, driver):
        self.open_register(driver)
        driver.find_element(By.ID, "pid").send_keys("123") # Quá ngắn
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        
        err = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        assert "Invalid ID length" in err