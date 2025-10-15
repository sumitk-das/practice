import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_logout(logged_in_browser):
    """Test the logout functionality"""
    # Since we're already logged in (thanks to the fixture),
    # just perform logout and verify
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.logout()
    
    # Verify we're back at the login page
    assert "saucedemo.com" in logged_in_browser.current_url, "Logout failed"
    print("Logout completed successfully")