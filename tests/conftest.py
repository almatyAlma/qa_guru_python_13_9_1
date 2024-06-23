import pytest
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
@pytest.fixture(scope="function", autouse=True)
def browser_params():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    browser.config.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield
    browser.quit()