import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module: General & Manage")
class TestGeneral:
    
    @allure.story("TC_HOME_03: External Links")
    def test_external_link(self, driver, base_url):
        driver.get(f"{base_url}/Page/HomePage.cshtml")
        driver.find_element(By.LINK_TEXT, "Contact").click()
        
        assert "Contact" in driver.page_source or "contact" in driver.current_url.lower()

    @allure.story("TC_PRICE_03: Check Price Table")
    def test_price_table(self, driver, base_url):
        driver.get(f"{base_url}/Page/TrainPriceListPage.cshtml")
        
        assert len(driver.find_elements(By.TAG_NAME, "tr")) > 0 or "Ticket Price" in driver.page_source