import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    services = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=services)
    driver .maximize_window()
    return driver

def login_test_with_id(driver):
    driver.get('https://www.saucedemo.com/')
    time.sleep(3)
    un = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(3)
    up = driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(3)
    login_btn = driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

def login_test_with_name(driver):
    driver.get('https://www.saucedemo.com/')
    time.sleep(3)
    un = driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(3)
    up = driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    time.sleep(3)
    login_btn = driver.find_element(By.NAME, "login-button").click()
    time.sleep(3)


def login_test_with_xpath(driver):
    driver.get('https://www.saucedemo.com/')
    time.sleep(3)
    un = driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("standard_user")
    time.sleep(3)
    up = driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("secret_sauce")
    time.sleep(3)
    login_btn = driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    time.sleep(3)

##Main
driver= setup_driver()
login_test_with_id(driver)
login_test_with_name(driver)
login_test_with_xpath(driver)

driver.quit()


