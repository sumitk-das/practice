import pytest
from pages.login_page import LoginPage

# Test Data
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USER = "invalid_user"
INVALID_PASSWORD = "invalid_pass"

@pytest.mark.smoke
def test_valid_login(browser):
    """Test login with valid credentials"""
    login_page = LoginPage(browser)
    
    # Go to login page and enter credentials
    login_page.navigate_to()
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # Verify login was successful
    assert login_page.is_login_successful(), "Login failed"
    print("Login successful with valid credentials")

@pytest.mark.regression
def test_invalid_login(browser):
    """Test login with invalid credentials"""
    login_page = LoginPage(browser)
    
    # Go to login page and enter invalid credentials
    login_page.navigate_to()
    login_page.login(INVALID_USER, INVALID_PASSWORD)
    
    # Verify login was not successful
    assert not login_page.is_login_successful(), "Login should have failed"
    print("Login correctly failed with invalid credentials")