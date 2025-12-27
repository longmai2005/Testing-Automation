import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.feature("Module: Login & Logout")
class TestAuth:
    VALID_USER = "cijnuj@ramcloud.us"
    VALID_PASS = "123456789"

    def js_click(self, driver, selector):
        """Click bằng JS để xuyên qua quảng cáo footer"""
        element = driver.find_element(By.CSS_SELECTOR, selector)
        driver.execute_script("arguments[0].click();", element)

    @allure.story("TC_LOG_02: Login thành công")
    def test_login_success(self, driver, base_url):
        driver.get(f"{base_url}/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys(self.VALID_USER)
        driver.find_element(By.ID, "password").send_keys(self.VALID_PASS)
        
        self.js_click(driver, "input[type='submit']")
        
        assert "Log out" in driver.page_source or "Welcome" in driver.page_source

    @allure.story("TC_LOG_FAIL: Login thất bại (Negative Test)")
    @pytest.mark.parametrize("email, password", [
        ("non_exist@gmail.com", "12345678"),
        ("cijnuj@ramcloud.us", "wrongpass"),
        ("", "12345678"),
        ("cijnuj@ramcloud.us", ""),
        ("<script>alert(1)</script>", "12345678"),
    ])
    def test_login_failure(self, driver, base_url, email, password):
        driver.get(f"{base_url}/Account/Login.cshtml")
        if email: driver.find_element(By.ID, "username").send_keys(email)
        if password: driver.find_element(By.ID, "password").send_keys(password)
        
        self.js_click(driver, "input[type='submit']")
        
        page_source = driver.page_source.lower()
        is_still_login_page = "login" in driver.title.lower()
        is_security_block = "potentially dangerous" in page_source
        is_validation_error = "invalid" in page_source or "required" in page_source
        
        assert is_still_login_page or is_security_block or is_validation_error

    @allure.story("TC_LOG_10: Login Locked")
    def test_login_locked(self, driver, base_url):
        driver.get(f"{base_url}/Account/Login.cshtml")
        for _ in range(6):
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys("lock_test@gmail.com")
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys("wrong")
            self.js_click(driver, "input[type='submit']")
            
            if "locked" in driver.page_source:
                break