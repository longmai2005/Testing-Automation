from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) 

    def do_click(self, locator):
        """Chờ element có thể click được rồi mới click"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        """Chờ element hiển thị rồi mới nhập text"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
        
    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    def wait_for_element(self, locator, timeout=10):
        """Chờ một element xuất hiện và trả về element đó"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )