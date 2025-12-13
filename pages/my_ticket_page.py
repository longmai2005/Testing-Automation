from selenium.webdriver.common.by import By
from base.base_page import BasePage

class MyTicketPage(BasePage):

    MY_TICKET_TABLE = (By.CSS_SELECTOR, "table.MyTable")

    CANCEL_BTN_FIRST_ROW = (By.XPATH, "//table[@class='MyTable']//tr[2]//input[@value='Cancel']")
    
    def get_all_rows(self):
        """Lấy tất cả các dòng vé đang hiển thị"""
        return self.driver.find_elements(By.CSS_SELECTOR, "table.MyTable tr")

    def cancel_first_ticket(self):
        """Hủy vé đầu tiên trong danh sách"""
        self.scroll_into_view(self.CANCEL_BTN_FIRST_ROW)
        self.do_click(self.CANCEL_BTN_FIRST_ROW)

        try:
            self.driver.switch_to.alert.accept()
        except:
            pass

    def is_ticket_displayed(self, depart_station, arrive_station):
        """Kiểm tra xem có vé đi từ A đến B trong bảng không"""
        rows = self.get_all_rows()
        for row in rows:
            if depart_station in row.text and arrive_station in row.text:
                return True
        return False