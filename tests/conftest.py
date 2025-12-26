import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# URL của trang web (Thay bằng URL thực tế của bài tập)
BASE_URL = "http://www.raillog.net/" 

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless") # Bỏ comment nếu muốn chạy ngầm
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get('driver')
        if driver_fixture:
            allure.attach(
                driver_fixture.get_screenshot_as_png(),
                name="Screenshot_Fail",
                attachment_type=allure.attachment_type.PNG
            )