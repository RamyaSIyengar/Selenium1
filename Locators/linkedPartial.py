import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

# serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
#
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/lenovo-thinkpad-x1-carbon-laptop")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Log").click()
time.sleep(2)

driver.close() #closes one browser at a time
#driver.quit() #closes all the browsers