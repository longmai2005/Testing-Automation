import pytest
import allure
from selenium.webdriver.common.by import By

@allure.feature("Module 3: Login")
class TestLogin:

    @allure.story("TC_LOG_02: Đăng nhập thành công")
    def test_login_success(self, driver):
        driver.get("http://www.raillog.net/Account/Login.cshtml")
        with allure.step("Nhập user/pass đúng"):
            driver.find_element(By.ID, "username").send_keys("test_user@gmail.com") # Thay bằng acc thật
            driver.find_element(By.ID, "password").send_keys("12345678")
            driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        
        with allure.step("Check chuyển trang"):
            assert "Welcome" in driver.page_source

    @allure.story("TC_LOG_06: Đăng nhập sai pass")
    def test_login_wrong_pass(self, driver):
        driver.get("http://www.raillog.net/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys("test_user@gmail.com")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        
        err = driver.find_element(By.CLASS_NAME, "error-msg").text # Thay locator lỗi
        assert "Invalid username or password" in err

    @allure.story("TC_LOG_10: Đăng nhập sai quá 5 lần (Account Locking)")
    def test_login_lock_account(self, driver):
        driver.get("http://www.raillog.net/Account/Login.cshtml")
        # Loop 5 lần
        for i in range(5):
            with allure.step(f"Lần nhập sai thứ {i+1}"):
                driver.find_element(By.ID, "username").send_keys("lock_user@gmail.com")
                driver.find_element(By.ID, "password").send_keys("wrong")
                driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
                driver.find_element(By.ID, "username").clear()
        
        with allure.step("Kiểm tra thông báo khóa"):
            err = driver.find_element(By.CLASS_NAME, "error-msg").text
            assert "locked" in err.lower()