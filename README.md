# Selenium Test Automation Project

This project demonstrates automated testing of a web application using Selenium
WebDriver with Python. The test suite covers various scenarios including login,
inventory management, checkout process, and order placement.

## Project Structure

```
selenium/
├── pages/                 # Page Object Models
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/                 # Test Cases
│   ├── conftest.py       # Test Configuration
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_order.py
├── utilities/            # Helper Functions
│   └── web_utils.py
├── pytest.ini           # PyTest Configuration
└── reports/            # Test Reports Directory
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

1. Run all tests with HTML report:

```bash
cd selenium
python -m pytest tests/ -v --html=reports/report.html
```

2. Run specific test file:

```bash
python -m pytest tests/test_login.py -v
```

3. Run tests with specific marker:

```bash
python -m pytest -v -m smoke  # Run smoke tests only
```

## Test Cases

The test suite includes the following scenarios:

- Login functionality (valid and invalid credentials)
- Adding products to cart
- Checkout process
- Order completion
- Logout functionality

## Reports

After test execution, you can find the HTML test report at:

```
selenium/reports/report.html
```

## Page Objects

The project follows the Page Object Model design pattern:

- `LoginPage`: Handles login-related actions and validations
- `InventoryPage`: Manages product listing and cart operations
- `CartPage`: Handles shopping cart functionality

## Utilities

- `web_utils.py`: Contains common web automation utilities and helper functions

## Best Practices

1. Use virtual environment for package management
2. Run tests from the `selenium` directory
3. Check the HTML report for detailed test execution results
4. Keep the ChromeDriver updated to match your Chrome browser version
