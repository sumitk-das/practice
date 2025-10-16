from selenium.webdriver.common.by import By
import time

class CartPage:
    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        time.sleep(1)

    def fill_information(self, firstname, lastname, zipcode):
        self.driver.find_element(*self.FIRST_NAME).send_keys(firstname)
        self.driver.find_element(*self.LAST_NAME).send_keys(lastname)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zipcode)
        time.sleep(1)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def complete_checkout(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(*self.BACK_TO_PRODUCTS).click()
        time.sleep(1)

    def cancel_checkout(self):
        """Cancel the checkout process"""
        self.driver.find_element(*self.CANCEL_BUTTON).click()
        time.sleep(1)
        print("Cancelled checkout")

    def continue_shopping(self):
        """Return to shopping from cart"""
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
        time.sleep(1)
        print("Continued shopping")