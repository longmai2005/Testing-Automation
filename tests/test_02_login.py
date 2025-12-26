import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module 3: Login")
class TestLogin:

    @allure.story("TC_LOG_02: Đăng nhập thành công")
    def test_login_success(self, driver, base_url):
        driver.get(base_url + "/Account/Login.cshtml")
        
        with allure.step("Nhập thông tin đúng"):
            driver.find_element(By.ID, "username").send_keys("cijnuj@ramcloud.us") 
            driver.find_element(By.ID, "password").send_keys("123456789")
            driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        
        with allure.step("Kiểm tra đăng nhập thành công"):
            assert len(driver.find_elements(By.LINK_TEXT, "Log out")) > 0

    @allure.story("TC_LOG_06: Đăng nhập sai pass")
    def test_login_wrong_pass(self, driver, base_url):
        driver.get(base_url + "/Account/Login.cshtml")
        
        driver.find_element(By.ID, "username").send_keys("longmai2005@gmail.com")
        driver.find_element(By.ID, "password").send_keys("saipassroi")
        driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        
        with allure.step("Kiểm tra báo lỗi"):
            error_msg = driver.find_element(By.CLASS_NAME, "message").text
            assert "Invalid username or password" in error_msg