import pytest
import allure
from selenium.webdriver.common.by import By
from tests.conftest import BASE_URL

@allure.feature("Module 1, 6, 7: Home - Timetable - Price")
class TestGeneralInfo:
    
    @allure.story("TC_HOME_01: Kiểm tra giao diện Home")
    def test_home_ui(self, driver):
        driver.get(BASE_URL)
        with allure.step("Kiểm tra tiêu đề và các tab chính"):
            assert "Railway" in driver.title
            # Thay locator tương ứng
            assert driver.find_element(By.LINK_TEXT, "Home").is_displayed()

    @allure.story("TC_HOME_02 -> 03: Điều hướng Tab")
    def test_navigation(self, driver):
        driver.get(BASE_URL)
        with allure.step("Click vào tab Timetable"):
            driver.find_element(By.LINK_TEXT, "Timetable").click()
            assert "Timetable" in driver.current_url

    @allure.story("TC_TIME_03: Kiểm tra giá vé từ Timetable")
    def test_check_price_from_timetable(self, driver):
        driver.get(BASE_URL + "/Page/TrainTimeListPage.cshtml")
        with allure.step("Click Check Price"):
            # Tìm nút check price dòng đầu tiên
            driver.find_element(By.XPATH, "//table//tr[2]//a[contains(text(),'Check Price')]").click()
            assert "TicketPrice" in driver.current_url

    @allure.story("TC_PRICE_04: Click Book Ticket khi chưa login")
    def test_book_ticket_no_login(self, driver):
        driver.get(BASE_URL + "/Page/TrainPriceListPage.cshtml")
        with allure.step("Click Book Ticket"):
            driver.find_element(By.LINK_TEXT, "Book ticket").click()
            # Mong đợi chuyển về trang Login
            assert "Login" in driver.current_url or "Login" in driver.title