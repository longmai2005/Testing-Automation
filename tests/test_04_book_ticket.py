import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

@allure.feature("Module 4: Book Ticket")
class TestBookTicket:

    def login_precondition(self, driver, base_url):
        driver.get(base_url + "/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys("longmai2005@gmail.com") 
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()

    @allure.story("TC_BOOK_03: Đặt vé ngày hợp lệ")
    def test_book_valid_date(self, driver, base_url):
        self.login_precondition(driver, base_url)
        
        driver.get(base_url + "/Page/BookTicketPage.cshtml")
        
        with allure.step("Chọn ngày đi (Ngày mai + 4 ngày)"):
            target_date = (datetime.now() + timedelta(days=4))
            formatted_date = f"{target_date.month}/{target_date.day}/{target_date.year}"
            
            date_dropdown = Select(driver.find_element(By.NAME, "Date"))
            try:
                date_dropdown.select_by_visible_text(formatted_date)
            except:

                date_dropdown.select_by_index(1)

        with allure.step("Chọn Ga đi / Ga đến"):
            Select(driver.find_element(By.NAME, "DepartStationId")).select_by_index(1)
            import time
            time.sleep(1) 
            Select(driver.find_element(By.NAME, "ArriveStationId")).select_by_index(1)
            Select(driver.find_element(By.NAME, "SeatType")).select_by_index(1)
            Select(driver.find_element(By.NAME, "TicketAmount")).select_by_visible_text("1")

        with allure.step("Submit vé"):
            driver.find_element(By.CSS_SELECTOR, "input[value='Book ticket']").click()
        
            assert "Success" in driver.current_url or "ManageTicket" in driver.current_url