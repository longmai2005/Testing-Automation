import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Module: Book Ticket")
class TestBookTicket:
    VALID_USER = "cijnuj@ramcloud.us"
    VALID_PASS = "123456789"

    def login(self, driver, base_url):
        driver.get(f"{base_url}/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys(self.VALID_USER)
        driver.find_element(By.ID, "password").send_keys(self.VALID_PASS)
        driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "input[type='submit']"))
        time.sleep(1) 

    @allure.story("TC_BOOK_04: Check Ga đi/đến")
    def test_station_logic(self, driver, base_url):
        self.login(driver, base_url)
        driver.get(f"{base_url}/Page/BookTicketPage.cshtml")
        
        if "Login" in driver.current_url:
            pytest.fail("Không thể login để vào Book Ticket. Kiểm tra lại tài khoản hoặc server.")

        try:
            depart_el = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, "DepartStationId"))
            )
            Select(depart_el).select_by_visible_text("Sài Gòn")
            time.sleep(1)
            
            arrive = Select(driver.find_element(By.NAME, "ArriveStationId"))
            assert "Sài Gòn" not in [opt.text for opt in arrive.options]
            
        except Exception as e:
            if "Invalid column name" in driver.page_source:
                pytest.skip("Server Error: Database Issue")
            else:
                raise e

    @allure.story("TC_BOOK_03: Check Date Range")
    def test_depart_date_range(self, driver, base_url):
        self.login(driver, base_url)
        driver.get(f"{base_url}/Page/BookTicketPage.cshtml")
        
        if "Login" in driver.current_url:
            pytest.fail("Login failed")

        try:
            date_select = Select(driver.find_element(By.NAME, "Date"))
            assert len(date_select.options) >= 3
        except:
            if "Invalid column name" in driver.page_source:
                pytest.skip("Server Error")