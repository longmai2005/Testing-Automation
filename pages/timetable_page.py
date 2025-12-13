from selenium.webdriver.common.by import By
from base.base_page import BasePage

class TimetablePage(BasePage):
    # Locators
    TIMETABLE_TABLE = (By.CSS_SELECTOR, "table.MyTable")
    
    def get_all_rows(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "table.MyTable tr")

    def click_check_price(self, depart, arrive):
        """Click vào link 'Check Price' của chuyến đi cụ thể"""
        xpath = f"//td[text()='{depart}']/following-sibling::td[text()='{arrive}']/..//a[contains(text(),'Check Price')]"
        self.scroll_into_view((By.XPATH, xpath))
        self.do_click((By.XPATH, xpath))

    def click_book_ticket(self, depart, arrive):
        """Click vào link 'Book ticket' của chuyến đi cụ thể"""
        xpath = f"//td[text()='{depart}']/following-sibling::td[text()='{arrive}']/..//a[contains(text(),'Book ticket')]"
        self.scroll_into_view((By.XPATH, xpath))
        self.do_click((By.XPATH, xpath))