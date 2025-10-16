from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import logging

logger = logging.getLogger(__name__)

def test_cancel_from_cart(browser):
    # Test Data
    username = "standard_user"
    password = "secret_sauce"

    # Initialize Page Objects
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)

    # Login
    logger.info("Logging in")
    login_page.navigate_to()
    login_page.login(username, password)
    assert login_page.is_login_successful(), "Login failed"

    # Add product and navigate to cart
    logger.info("Adding product and testing cancel")
    inventory_page.add_product1_to_cart()
    inventory_page.go_to_cart()
    cart_page.start_checkout()
    cart_page.cancel_checkout()

def test_continue_shopping(browser):
    # Test Data
    username = "standard_user"
    password = "secret_sauce"

    # Initialize Page Objects
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)

    # Login
    logger.info("Logging in")
    login_page.navigate_to()
    login_page.login(username, password)
    assert login_page.is_login_successful(), "Login failed"

    # Add product and test continue shopping
    logger.info("Adding product and testing continue shopping")
    inventory_page.add_product1_to_cart()
    inventory_page.go_to_cart()
    cart_page.continue_shopping()
    # Add another product to verify we're back at inventory
    inventory_page.add_product2_to_cart()