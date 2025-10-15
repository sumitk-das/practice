import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_add_single_product(logged_in_browser):
    """Test adding a single product to the cart"""
    # Add first product to cart
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.add_product1_to_cart()
    
    # Go to cart to verify
    inventory_page.go_to_cart()
    assert "cart" in logged_in_browser.current_url
    print("Successfully added single product to cart")

@pytest.mark.regression
def test_add_products_in_sequence(logged_in_browser):
    """Test adding multiple products to the cart one after another"""
    # Initialize page
    inventory_page = InventoryPage(logged_in_browser)
    
    # Add first product
    inventory_page.add_product1_to_cart()
    print("First product added successfully")
    
    # Add second product
    inventory_page.add_product2_to_cart()
    print("Second product added successfully")
    
    # Verify by going to cart
    inventory_page.go_to_cart()
    assert "cart" in logged_in_browser.current_url
    print("Successfully added both products to cart")