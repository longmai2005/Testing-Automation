import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module: Timetable & Ticket Price")
class TestInfo:
    
    @allure.story("TC_TIME_01: Verify Timetable UI & Check Price")
    def test_timetable(self, driver, base_url):
        driver.get(f"{base_url}/Page/TrainTimeListPage.cshtml")
        
        with allure.step("Click Check Price"):
            check_price_btns = driver.find_elements(By.XPATH, "//a[contains(text(),'Check Price')]")
            if check_price_btns:
                check_price_btns[0].click()
                assert "TicketPrice" in driver.current_url
    
    @allure.story("TC_PRICE_04: Redirect to Login from Ticket Price")
    def test_price_book_redirect(self, driver, base_url):
        driver.delete_all_cookies() 
        driver.get(f"{base_url}/Page/TrainPriceListPage.cshtml")
        
        with allure.step("Click Book Ticket"):
            book_btns = driver.find_elements(By.XPATH, "//a[contains(text(),'Book ticket')]")
            if book_btns:
                book_btns[0].click()
                assert "Login" in driver.current_url