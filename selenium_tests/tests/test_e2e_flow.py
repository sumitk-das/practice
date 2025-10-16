import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import logging

logger = logging.getLogger(__name__)

# Test Data
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
PRODUCT_DATA = {
    "firstname": "John",
    "lastname": "Doe",
    "zipcode": "12345"
}

@pytest.mark.step1_login
def test_01_valid_login(browser):
    """Test valid login credentials"""
    login_page = LoginPage(browser)
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    assert login_page.is_login_successful(), "Login failed"
    logger.info("Login successful")

@pytest.mark.step2_inventory
def test_02_add_products(browser):
    """Test adding multiple products to cart"""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    
    # Login first
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # Add products
    inventory_page.add_product1_to_cart()
    inventory_page.add_product2_to_cart()
    logger.info("Products added to cart")

@pytest.mark.step3_order
def test_03_complete_order(browser):
    """Test completing an order with multiple products"""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    
    # Login first
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # Add products and checkout
    inventory_page.add_product1_to_cart()
    inventory_page.add_product2_to_cart()
    inventory_page.go_to_cart()
    
    # Complete checkout
    cart_page.start_checkout()
    cart_page.fill_information(
        PRODUCT_DATA["firstname"],
        PRODUCT_DATA["lastname"],
        PRODUCT_DATA["zipcode"]
    )
    cart_page.complete_checkout()
    logger.info("Order completed successfully")

@pytest.mark.step4_remove
def test_04_remove_products(browser):
    """Test removing products from cart"""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    
    # Login first
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # Add and remove products
    inventory_page.add_product1_to_cart()
    inventory_page.add_product2_to_cart()
    inventory_page.remove_product1_from_cart()
    inventory_page.remove_product2_from_cart()
    logger.info("Products removed from cart")

@pytest.mark.step5_cancel
def test_05_cancel_order(browser):
    """Test canceling an order and continuing shopping"""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    
    # Login first
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # Add product and test cancellation
    inventory_page.add_product1_to_cart()
    inventory_page.go_to_cart()
    cart_page.start_checkout()
    cart_page.cancel_checkout()
    
    # Test continue shopping
    cart_page.continue_shopping()
    inventory_page.add_product2_to_cart()
    logger.info("Order canceled and continued shopping")

@pytest.mark.step6_logout
def test_06_logout(browser):
    """Test logout functionality"""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    
    # Login first
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # Logout
    inventory_page.logout()
    logger.info("Logged out successfully")