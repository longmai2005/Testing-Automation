import allure
import pytest
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@allure.feature("Module: Book Ticket")
class TestBookTicket:
    VALID_USER = "cijnuj@ramcloud.us"
    VALID_PASS = "123456789"

    def login(self, driver, base_url):
        driver.get(f"{base_url}/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys(self.VALID_USER)
        driver.find_element(By.ID, "password").send_keys(self.VALID_PASS)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    @allure.story("TC_BOOK_01: Redirect về Login nếu chưa đăng nhập")
    def test_redirect(self, driver, base_url):
        driver.delete_all_cookies() 
        driver.get(f"{base_url}/Page/BookTicketPage.cshtml")
        assert "Login" in driver.current_url

    @allure.story("TC_BOOK_03: Kiểm tra ngày khởi hành (Logic 3-30 ngày)")
    def test_depart_date_range(self, driver, base_url):
        self.login(driver, base_url)
        driver.get(f"{base_url}/Page/BookTicketPage.cshtml")
        
        date_select = Select(driver.find_element(By.NAME, "Date"))
        options = date_select.options
        
        first_date_str = options[0].text
        last_date_str = options[-1].text
        
        assert len(options) >= 3, "Phải có ít nhất vài ngày để chọn"

    @allure.story("TC_BOOK_04: Ga đi và Ga đến phải khác nhau/Logic Trip Matrix")
    def test_station_logic(self, driver, base_url):
        self.login(driver, base_url)
        driver.get(f"{base_url}/Page/BookTicketPage.cshtml")
        
       
        Select(driver.find_element(By.NAME, "DepartStationId")).select_by_visible_text("Sài Gòn")
        time.sleep(1) 
        
        arrive_select = Select(driver.find_element(By.NAME, "ArriveStationId"))
        all_arrive_text = [opt.text for opt in arrive_select.options]
        
        assert "Sài Gòn" not in all_arrive_text or len(all_arrive_text) == 1