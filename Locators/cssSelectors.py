"""
CSS Selectors
Tag and id
tag and OOPS
tag and attribute
tag OOPS and attribute
"""
import time

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

# 1. tagName#idValue
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("7090929039")
# tagname is optional, you can just add #idvalue
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("7090929039")


# 2. tag and OOPS
driver.find_element(By.CSS_SELECTOR, "input._9npi").send_keys("R6i#24412")

# 3. tag and attribute => tagName[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# 4. tag OOPS and attribute    tagname.OOPS[attribute=value]
driver.find_element(By.CSS_SELECTOR, "button._42ft[type=submit]").click()

time.sleep(5)

