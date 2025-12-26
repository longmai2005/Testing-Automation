import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module: Login & Logout")
class TestAuth:
    VALID_USER = "cijnuj@ramcloud.us"
    VALID_PASS = "123456789"

    @allure.story("TC_LOG_02: Login thành công")
    def test_login_success(self, driver, base_url):
        driver.get(f"{base_url}/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys(self.VALID_USER)
        driver.find_element(By.ID, "password").send_keys(self.VALID_PASS)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        assert "Welcome" in driver.page_source or "Log out" in driver.page_source

    @allure.story("TC_LOG_03 -> 08: Các trường hợp Login thất bại")
    @pytest.mark.parametrize("email, password, expected_error", [
        ("non_exist@gmail.com", "12345678", "Invalid username or password"), 
        ("cijnuj@ramcloud.us", "wrongpass", "Invalid username or password"), 
        ("", "12345678", "The Email field is required"),                     
        ("cijnuj@ramcloud.us", "", "The Password field is required"),        
        ("<script>alert(1)</script>", "12345678", "Invalid"),                
    ])
    def test_login_failure(self, driver, base_url, email, password, expected_error):
        driver.get(f"{base_url}/Account/Login.cshtml")
        if email: driver.find_element(By.ID, "username").send_keys(email)
        if password: driver.find_element(By.ID, "password").send_keys(password)
        
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        
        page_source = driver.page_source
        assert expected_error in page_source or "Invalid" in page_source

    @allure.story("TC_LOG_10: Login Locked (5 lần)")
    def test_login_locked(self, driver, base_url):
        driver.get(f"{base_url}/Account/Login.cshtml")
        for _ in range(6):
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys("lock_test@gmail.com")
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys("wrong")
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
            
            if "locked" in driver.page_source:
                break