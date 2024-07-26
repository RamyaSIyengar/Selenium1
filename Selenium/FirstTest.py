import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()

# Creates a new instance of the chrome driver. Starts the service and then creates new instance of chrome driver.

try:
    # Open the OrangeHRM demo page
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Wait for the username field to be present and enter the username - explicit waiting
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("Admin")

    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys("admin123")

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button"))
    )
    login_button.click()
    time.sleep(5)

finally:
    # Close the browser
    act_title = driver.title
    exp_title = "OrangeHRM"
    if act_title == exp_title:
        print("Test passed")
    else:
        print("test failed")

    driver.close()