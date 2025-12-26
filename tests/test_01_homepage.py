import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module 1, 6, 7: Home - Timetable - Price")
class TestGeneralInfo:
    
    @allure.story("TC_HOME_01: Kiểm tra giao diện Home")
    def test_home_ui(self, driver, base_url): 
        driver.get(base_url + "/Page/HomePage.cshtml")
        
        with allure.step("Kiểm tra tiêu đề"):
            assert "Safe Railway" in driver.title 
            
        with allure.step("Kiểm tra Tab hiển thị"):
            assert driver.find_element(By.LINK_TEXT, "Timetable").is_displayed()
            assert driver.find_element(By.LINK_TEXT, "Ticket price").is_displayed()

    @allure.story("TC_TIME_03: Kiểm tra giá vé từ Timetable")
    def test_check_price_from_timetable(self, driver, base_url):
        driver.get(base_url + "/Page/TrainTimeListPage.cshtml")
        
        with allure.step("Click Check Price ở dòng đầu tiên"):
            btns = driver.find_elements(By.XPATH, "//table//a[contains(text(),'Check Price')]")
            if len(btns) > 0:
                btns[0].click()
                assert "TicketPrice" in driver.current_url
            else:
                pytest.skip("Không tìm thấy chuyến tàu nào để check giá")

    @allure.story("TC_PRICE_04: Click Book Ticket khi chưa login")
    def test_book_ticket_no_login(self, driver, base_url):
        driver.get(base_url + "/Page/TrainPriceListPage.cshtml")
        
        with allure.step("Click link Book ticket"):
            driver.find_element(By.LINK_TEXT, "Book ticket").click()
            
            assert "Login" in driver.current_url