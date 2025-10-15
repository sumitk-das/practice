from selenium.webdriver.common.by import By
import time

class LoginPage:
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(2)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)

    def is_login_successful(self):
        return "inventory" in self.driver.current_url