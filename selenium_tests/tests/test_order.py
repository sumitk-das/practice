import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Test Data
CUSTOMER_INFO = {
    "firstname": "Sumit",
    "lastname": "Das",
    "zipcode": "1234"
}

@pytest.mark.smoke
def test_complete_single_product_order(logged_in_browser):
    """Test completing an order with a single product"""
    # Add one product to cart
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.add_product1_to_cart()
    inventory_page.go_to_cart()
    
    # Complete checkout process
    cart_page = CartPage(logged_in_browser)
    cart_page.start_checkout()
    cart_page.fill_information(
        CUSTOMER_INFO["firstname"],
        CUSTOMER_INFO["lastname"],
        CUSTOMER_INFO["zipcode"]
    )
    cart_page.complete_checkout()
    
    assert "inventory" in logged_in_browser.current_url
    print("Single product order completed successfully")

@pytest.mark.regression
def test_complete_two_product_order(logged_in_browser):
    """Test completing an order with two products"""
    # Add both products to cart
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.add_product1_to_cart()
    inventory_page.add_product2_to_cart()
    inventory_page.go_to_cart()
    
    # Complete checkout process
    cart_page = CartPage(logged_in_browser)
    cart_page.start_checkout()
    cart_page.fill_information(
        CUSTOMER_INFO["firstname"],
        CUSTOMER_INFO["lastname"],
        CUSTOMER_INFO["zipcode"]
    )
    cart_page.complete_checkout()
    
    assert "inventory" in logged_in_browser.current_url
    print("Two product order completed successfully")