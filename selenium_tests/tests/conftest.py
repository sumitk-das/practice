import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Logger Setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Test Data
TEST_USER = "standard_user"
TEST_PASSWORD = "secret_sauce"

@pytest.fixture()
def browser():
    """Create a Chrome browser instance"""
    logger.info("Starting the browser")
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    logger.info("Closing the browser")
    driver.quit()

@pytest.fixture()
def logged_in_browser(browser):
    """Create a browser instance and log in to the application"""
    logger.info("Logging in to the application")
    login_page = LoginPage(browser)
    login_page.navigate_to()
    login_page.login(TEST_USER, TEST_PASSWORD)
    assert login_page.is_login_successful(), "Login failed"
    yield browser