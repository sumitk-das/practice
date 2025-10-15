import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

def setup_driver():
    services = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=services)
    driver .maximize_window()
    return driver


# def input_field(driver):
#     driver.get('https://demoqa.com/text-box')
#     time.sleep(2)
#     name = driver.find_element(By.ID, "userName").send_keys("Sumit Das")
#     time.sleep(1)
#     email = driver.find_element(By.ID, "userEmail").send_keys("hi@sumitkdas.pro")
#     time.sleep(1)
#     current_address = driver.find_element(By.ID, "currentAddress").send_keys("Dhaka, Bangladesh")
#     time.sleep(1)
#     permanent_address = driver.find_element(By.ID, "permanentAddress").send_keys("Jashore, Bangladesh")
#     time.sleep(1)
#     submit_button = driver.find_element(By.ID, "submitButton").click()
#     time.sleep(5)
#
# def radio_button(driver):
#     driver.get('https://demoqa.com/radio-button')
#     time.sleep(2)
#     select_yes = driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
#     time.sleep(1)
#     select_impressive = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']").click()
#     time.sleep(1)
#
# def check_box(driver):
#     driver.get('https://demoqa.com/checkbox')
#     time.sleep(2)
#     check = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']").click()
#     time.sleep(2)
#     uncheck = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']").click()
#     time.sleep(2)

# Need to understand more
def button_test(driver):
    driver.get('https://demoqa.com/buttons')
    time.sleep(2)
    double_click_btn = driver.find_element(By.ID, 'doubleClickBtn')
    ActionChains(driver).double_click(double_click_btn).perform()
    time.sleep(2)
    right_click_btn = driver.find_element(By.ID, 'rightClickBtn')
    ActionChains(driver).context_click(right_click_btn).perform()
    time.sleep(2)
    dynamic_click_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]")
    dynamic_click_btn.click()
    print("✅ Button test completed successfully")


if __name__ == "__main__":
    driver = setup_driver()
    try:
        # input_field(driver)
        # radio_button(driver)
        # check_box(driver)
        button_test(driver)
    finally:
        driver.quit()
