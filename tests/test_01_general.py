import allure
import pytest
from selenium.webdriver.common.by import By

@allure.feature("Module: Home & FAQ")
class TestHomeFAQ:

    @allure.story("TC_HOME_01: UI Home Page & Navigation")
    def test_home_ui_navigation(self, driver, base_url):
        driver.get(f"{base_url}/Page/HomePage.cshtml")
        with allure.step("Kiểm tra Title và Tab chính"):
            assert "Safe Railway" in driver.title
            assert driver.find_element(By.LINK_TEXT, "Home").is_displayed()
            assert driver.find_element(By.LINK_TEXT, "FAQ").is_displayed()
            assert driver.find_element(By.LINK_TEXT, "Contact").is_displayed()

    @allure.story("TC_HOME_02: User chưa login không thể vào tab Book Ticket")
    def test_restricted_tabs(self, driver, base_url):
        driver.get(f"{base_url}/Page/HomePage.cshtml")
        with allure.step("Click Book Ticket khi chưa login"):
            driver.find_element(By.LINK_TEXT, "Book ticket").click()
            assert "Login" in driver.current_url or "Login" in driver.title

    @allure.story("TC_FAQ_01: Verify UI FAQ Page")
    def test_faq_ui(self, driver, base_url):
        driver.get(f"{base_url}/Page/FAQ.cshtml")
        with allure.step("Kiểm tra danh sách câu hỏi"):
            questions = driver.find_elements(By.CLASS_NAME, "faq-question")
            assert "FAQ" in driver.page_source

    @allure.story("TC_FAQ_03: Verify Embedded Links in FAQ")
    def test_faq_links(self, driver, base_url):
        driver.get(f"{base_url}/Page/FAQ.cshtml")
        links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Register")
        if links:
            links[0].click()
            assert "Register" in driver.current_url