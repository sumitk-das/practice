from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging

logger = logging.getLogger(__name__)

def test_remove_single_product(browser):
    # Test Data
    username = "standard_user"
    password = "secret_sauce"

    # Initialize Page Objects
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)

    # Login
    logger.info("Logging in")
    login_page.navigate_to()
    login_page.login(username, password)
    assert login_page.is_login_successful(), "Login failed"

    # Add and remove product
    logger.info("Adding and removing product")
    inventory_page.add_product1_to_cart()
    inventory_page.remove_product1_from_cart()

def test_remove_multiple_products(browser):
    # Test Data
    username = "standard_user"
    password = "secret_sauce"

    # Initialize Page Objects
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)

    # Login
    logger.info("Logging in")
    login_page.navigate_to()
    login_page.login(username, password)
    assert login_page.is_login_successful(), "Login failed"

    # Add and remove multiple products
    logger.info("Adding and removing multiple products")
    inventory_page.add_product1_to_cart()
    inventory_page.add_product2_to_cart()
    inventory_page.remove_product2_from_cart()
    inventory_page.remove_product1_from_cart()