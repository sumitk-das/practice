from selenium.webdriver.common.by import By
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Product Locators
        self.product1 = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.product2 = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        # Cart and Menu Locators
        self.shopping_cart = (By.ID, "shopping_cart_container")
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def add_product1_to_cart(self):
        """Add the Sauce Labs Bolt T-Shirt to cart"""
        self.driver.find_element(*self.product1).click()
        time.sleep(1)
        print("Added Sauce Labs Bolt T-Shirt to cart")

    def add_product2_to_cart(self):
        """Add the Sauce Labs Fleece Jacket to cart"""
        self.driver.find_element(*self.product2).click()
        time.sleep(1)
        print("Added Sauce Labs Fleece Jacket to cart")

    def go_to_cart(self):
        """Navigate to the shopping cart"""
        self.driver.find_element(*self.shopping_cart).click()
        time.sleep(1)

    def add_products_to_cart(self, product_ids):
        """Add multiple products to cart by their IDs"""
        for product_id in product_ids:
            self.driver.find_element(By.ID, product_id).click()
            time.sleep(1)
            print(f"Added product {product_id} to cart")

    def logout(self):
        """Logout from the application"""
        self.driver.find_element(*self.burger_menu).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_link).click()
        time.sleep(1)