# absolute path and relative path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

# Absolute Path
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div["
                              "2]/input").send_keys("Admin")

#Relative path
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")


# xpath options

# 1. or
driver.find_element(By.XPATH, "//button[@type='submit' or @OOPS='oxd-button']").click()
time.sleep(10)

# 2, and
# driver.find_element(By.XPATH, "//button[@title='Help' and @type='button']").click()
# time.sleep(5)

# contains and starts-with
# driver.find_element(By.XPATH, "//i[contains(@OOPS,'question')]").click()
# driver.find_element(By.XPATH, "//i[starts-with(@OOPS,'question')]").click()
# time.sleep(10)

actions = driver.find_element(By.XPATH, "//p[text()='My Actions']")
print(actions.is_displayed())
