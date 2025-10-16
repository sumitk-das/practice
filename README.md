# Selenium Test Automation Project

This project demonstrates automated testing of a web application using Selenium
WebDriver with Python. The test suite covers various scenarios including login,
inventory management, checkout process, order placement, and cart operations.

## Project Structure

```
selenium_tests/
├── pages/                 # Page Object Models
│   ├── cart_page.py      # Shopping cart operations
│   ├── inventory_page.py # Product and inventory management
│   └── login_page.py     # Authentication handling
├── tests/                # Test Cases
│   ├── conftest.py      # Test Configuration
│   ├── test_cart_navigation.py
│   ├── test_checkout.py
│   ├── test_e2e_flow.py # Sequential end-to-end tests
│   ├── test_inventory.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_order.py
│   └── test_remove_products.py
├── pytest.ini          # PyTest Configuration
└── reports/           # Test Reports Directory
    └── report.html
```

## Requirements

- Python 3.x
- Google Chrome Browser
- Virtual Environment (recommended)

## Setup Instructions

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

2. Install required packages:

```bash
pip install pytest selenium pytest-html webdriver-manager
```

## Running Tests

### Sequential End-to-End Testing

Run the complete test flow in sequence:

```bash
cd selenium_tests
python -m pytest tests/test_e2e_flow.py -v --html=reports/report.html
```

The sequential tests run in this order:

1. Login functionality
2. Add products to cart
3. Complete order process
4. Remove products from cart
5. Cancel order and continue shopping
6. Logout

You can also run a specific step using markers:

```bash
python -m pytest -v -m step1_login    # Run only login tests
python -m pytest -v -m step2_inventory # Run only inventory tests
```

### Individual Test Execution

1. Run all tests with HTML report:

```bash
cd selenium_tests
python -m pytest tests/ -v --html=reports/report.html
```

2. Run specific test file:

```bash
python -m pytest tests/test_login.py -v
```

## Test Scenarios

The test suite includes comprehensive testing of:

1. Authentication

   - Valid and invalid login attempts
   - Logout functionality

2. Shopping Cart Operations

   - Adding products to cart
   - Removing products from cart
   - Cart navigation (continue shopping, cancel)

3. Checkout Process

   - Complete order placement
   - Order cancellation
   - Information validation

4. End-to-End Workflows
   - Sequential test flow from login to logout
   - Multiple product handling
   - Order completion and cancellation

## Reports

After test execution, you can find the HTML test report at:

```
selenium/reports/report.html
```

## Page Object Model

The project follows the Page Object Model (POM) design pattern for better
maintainability:

### `LoginPage`

- Authentication handling
- Login status validation
- Navigation to login page

### `InventoryPage`

- Product management
- Add/remove products from cart
- Menu navigation
- Logout functionality

### `CartPage`

- Shopping cart operations
- Checkout process
- Order completion
- Continue shopping functionality

## Test Organization

1. **Independent Test Files**

   - Separate test files for each functionality
   - Modular and maintainable test structure
   - Easy to run specific test categories

2. **Sequential Testing**
   - `test_e2e_flow.py` for ordered test execution
   - Step-by-step validation of complete user journey
   - Clearly marked test sequence

- `web_utils.py`: Contains common web automation utilities and helper functions

## Best Practices

1. Use virtual environment for package management
2. Run tests from the `selenium` directory
3. Check the HTML report for detailed test execution results
4. Keep the ChromeDriver updated to match your Chrome browser version
