import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# driver.save_screenshot(os.getcwd() + "\\homepage.png")
driver.get_screenshot_as_file(os.getcwd() + "\\homepage.png")

# driver.get_screenshot_as_png() # in ascii code we need to decode
# driver.get_screenshot_as_base64() # saves in binary
driver.quit()
