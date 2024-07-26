import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:\Drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(15)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()


# 1 prompt - text ok/cancel

# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# alertWindow = driver.switch_to.alert
# alertWindow.send_keys("Hello")
#
# alertWindow.dismiss()
# alertWindow.accept()
# time.sleep(5)

# 2 confirm ok/cancel
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
# alertWindow = driver.switch_to.alert
#
# # alertWindow.accept()
# alertWindow.dismiss()
#
# time.sleep(5)


# 3 Alert - ok

# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
# driver.switch_to.alert.accept()
# time.sleep(5)


# 4  Authenticated popups
# popup for login to application like DEXT, where we can switch_to alert as its a additional authentication 
# to bypass the popup, we can specify username and password with the url itself

# https://the-internet.herokuapp.com/basic_auth
# https://username:password@url
# https://admin:admin@the-internet.herokuapp.com/basic_auth




