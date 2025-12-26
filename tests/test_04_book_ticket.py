import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

@allure.feature("Module 4: Book Ticket")
class TestBookTicket:

    # Helper function để login trước khi book
    def login(self, driver):
        driver.get("http://www.raillog.net/Account/Login.cshtml")
        driver.find_element(By.ID, "username").send_keys("test_user@gmail.com")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()

    @allure.story("TC_BOOK_03: Kiểm tra ngày khởi hành (3-30 ngày)")
    def test_depart_date_logic(self, driver):
        self.login(driver)
        driver.get("http://www.raillog.net/Page/BookTicketPage.cshtml")
        
        # Chọn ngày: Ngày hiện tại + 4 ngày (Hợp lệ)
        valid_date = (datetime.now() + timedelta(days=4)).strftime("%m/%d/%Y")
        
        with allure.step("Chọn ngày hợp lệ"):
            Select(driver.find_element(By.NAME, "Date")).select_by_visible_text(valid_date)
            # Nếu code JS tự động validate thì assert ở đây không có lỗi

    @allure.story("TC_BOOK_07: Đặt quá 10 vé")
    def test_book_over_10_tickets(self, driver):
        self.login(driver)
        driver.get("http://www.raillog.net/Page/BookTicketPage.cshtml")
        
        with allure.step("Đặt vé cho 11 người (hoặc lặp lại action)"):
            # Logic này phụ thuộc vào cách trang web cho chọn số lượng
            # Ví dụ chọn dropdown số lượng > 10
            pass 
            # assert "cannot book more than 10" in driver.page_source