import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Logger Setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@pytest.fixture()
def browser():
    logger.info("Step 1: Open the browser")
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_login(browser):
    # Test Data
    username = "standard_user"
    password = "secret_sauce"
    firstname = "Sumit"
    lastname = "Das"
    zipcode = "1234"
    products = ["add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket"]

    # Initialize Page Objects
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)

    # Login
    logger.info("Logging in")
    login_page.navigate_to()
    login_page.login(username, password)
    assert login_page.is_login_successful(), "Login failed"
    print("Login Successful")

    # Add products to cart
    logger.info("Adding products to cart")
    inventory_page.add_products_to_cart(products)
    print(f"Added {len(products)} products to cart")

    # Go to cart and checkout
    logger.info("Proceeding to checkout")
    inventory_page.go_to_cart()
    assert "cart" in browser.current_url, "Failed to navigate to cart"
    print("Cart page loaded successfully")

    # Complete checkout process
    cart_page.start_checkout()
    assert "checkout-step-one" in browser.current_url, "Failed to start checkout"
    print("Redirected to your information page")

    cart_page.fill_information(firstname, lastname, zipcode)
    assert "checkout-step-two" in browser.current_url, "Failed to proceed to checkout step two"
    print("Information filled out")

    cart_page.complete_checkout()
    assert "inventory" in browser.current_url, "Failed to complete checkout"
    print("Checkout Complete")

    # Logout
    logger.info("Logging out")
    inventory_page.logout()
    assert "saucedemo.com" in browser.current_url, "Failed to logout"
    print("Logout Successful")