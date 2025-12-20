from selenium.webdriver.common.by import By
from base.base_page import BasePage

class TimetablePage(BasePage):
    TIMETABLE_TABLE = (By.CSS_SELECTOR, "table.MyTable")
    
    def get_all_rows(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "table.MyTable tr")

    def click_check_price(self, depart, arrive):
        xpath = f"//td[contains(text(), '{depart}')]/following-sibling::td[contains(text(), '{arrive}')]/..//a[contains(text(), 'Check Price')]"
        self.scroll_into_view((By.XPATH, xpath))
        self.do_click((By.XPATH, xpath))

    def click_book_ticket(self, depart, arrive):
        xpath = f"//td[contains(text(), '{depart}')]/following-sibling::td[contains(text(), '{arrive}')]/..//a[contains(text(), 'Book ticket')]"
        self.scroll_into_view((By.XPATH, xpath))
        self.do_click((By.XPATH, xpath))