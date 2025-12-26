import allure
import pytest
import time
from selenium.webdriver.common.by import By

@allure.feature("Module 2: Register")
class TestRegister:

    @allure.story("TC_REG_02: Đăng ký tài khoản mới")
    def test_register_success(self, driver, base_url):
        driver.get(base_url + "/Account/Register.cshtml")
        
        new_email = f"auto_{int(time.time())}@gmail.com"
        
        with allure.step(f"Đăng ký với email: {new_email}"):
            driver.find_element(By.ID, "email").send_keys(new_email)
            driver.find_element(By.ID, "password").send_keys("12345678")
            driver.find_element(By.ID, "confirmPassword").send_keys("12345678")
            driver.find_element(By.ID, "pid").send_keys("123456789")
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
            
        with allure.step("Kiểm tra thành công"):
 
            assert "Login" in driver.current_url or "Welcome" in driver.page_source