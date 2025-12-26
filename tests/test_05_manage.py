import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module: General (Home, FAQ, Timetable)")
class TestGeneral:
    
    @allure.story("TC_HOME_03: External Links")
    def test_external_link(self, driver, base_url):
        driver.get(f"{base_url}/Page/HomePage.cshtml")
    
        driver.find_element(By.LINK_TEXT, "Contact").click()
        assert "Contact" in driver.title

    @allure.story("TC_FAQ_02: FAQ Accordion Behavior")
    def test_faq_behavior(self, driver, base_url):
        driver.get(f"{base_url}/Page/FAQ.cshtml")
        questions = driver.find_elements(By.CLASS_NAME, "question")
        if questions:
            questions[0].click()
            assert questions[0].is_displayed()

    @allure.story("TC_TIME_02: Check Timetable")
    def test_timetable_display(self, driver, base_url):
        driver.get(f"{base_url}/Page/TrainTimeListPage.cshtml")
        rows = driver.find_elements(By.XPATH, "//table//tr")
        assert len(rows) > 1, "Bảng lịch trình phải có dữ liệu"

    @allure.story("TC_PRICE_03: Check Price Table")
    def test_price_table(self, driver, base_url):
        driver.get(f"{base_url}/Page/TrainPriceListPage.cshtml")
       
        assert "Ticket Price" in driver.title
        assert len(driver.find_elements(By.TAG_NAME, "table")) > 0