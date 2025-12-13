from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base.base_page import BasePage
import time

class BookTicketPage(BasePage):
    DEPART_DATE_SELECT = (By.NAME, 'Date')
    DEPART_STATION_SELECT = (By.NAME, 'DepartStation')
    ARRIVE_STATION_SELECT = (By.NAME, 'ArriveStation')
    SEAT_TYPE_SELECT = (By.NAME, 'SeatType')
    TICKET_AMOUNT_SELECT = (By.NAME, 'TicketAmount')
    BOOK_TICKET_BTN = (By.CSS_SELECTOR, 'input[value="Book ticket"]')

    def book_ticket(self, depart, arrive, seat, amount, date=None):
        
        element_date = self.driver.find_element(*self.DEPART_DATE_SELECT)
        select_date = Select(element_date)
        if date:
            select_date.select_by_visible_text(date)
        else:
            select_date.select_by_index(0)
            print(f"Auto-selected Date: {select_date.first_selected_option.text}")

        def select_option(locator, text):
            element = self.driver.find_element(*locator)
            select = Select(element)
            try:
                select.select_by_visible_text(text)
            except Exception:
                print(f"[DEBUG] Cannot find option: '{text}'")
                raise

        select_option(self.DEPART_STATION_SELECT, depart)
        time.sleep(1)
        select_option(self.ARRIVE_STATION_SELECT, arrive)
        select_option(self.SEAT_TYPE_SELECT, seat)
        select_option(self.TICKET_AMOUNT_SELECT, amount)
        
        print("Attempting to click Book Ticket button via JS...")
        book_btn = self.driver.find_element(*self.BOOK_TICKET_BTN)
        self.driver.execute_script("arguments[0].click();", book_btn)
        
        time.sleep(2)