import pytest
import allure
from selenium.webdriver.common.by import By

@allure.feature("Module 5 & 8: Management")
class TestManagement:
    
    def login(self, driver):
        driver.get("http://www.raillog.net/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys("test_user@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()

    @allure.story("TC_MYT_03: Hủy vé")
    def test_cancel_ticket(self, driver):
        self.login(driver)
        driver.get("http://www.raillog.net/Page/ManageTicket.cshtml")
        
        with allure.step("Tìm nút Cancel đầu tiên"):
            # Tìm nút cancel của vé đầu tiên trong bảng
            cancel_btn = driver.find_element(By.XPATH, "//table//tr[2]//input[@value='Cancel']")
            cancel_btn.click()
            
            # Xử lý alert nếu có
            driver.switch_to.alert.accept()
        
        with allure.step("Kiểm tra trạng thái"):
            # Verify nút đổi thành 'Cancelled' hoặc dòng đó biến mất
            pass

    @allure.story("TC_CP_04: Đổi mật khẩu không khớp")
    def test_change_pass_mismatch(self, driver):
        self.login(driver)
        driver.get("http://www.raillog.net/Account/ChangePassword.cshtml")
        
        driver.find_element(By.ID, "currentPassword").send_keys("12345678")
        driver.find_element(By.ID, "newPassword").send_keys("newpass123")
        driver.find_element(By.ID, "confirmPassword").send_keys("khongkhop")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        
        assert "do not match" in driver.page_source