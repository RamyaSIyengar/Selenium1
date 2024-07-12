import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# Application commands
print(driver.title)
print(driver.current_url)
print(driver.page_source)


# Conditional commands

searchBar = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status", searchBar.is_displayed())
print("Enabled Status", searchBar.is_enabled())  # can I type in it

male = (driver.find_element(By.XPATH, "//input[@id='gender-male']"))
female = (driver.find_element(By.XPATH, "//input[@id='gender-female']"))
print("before clicking on the radio button- ")
print(male.is_selected())
print(female.is_selected())

male.click()
print("after clicking on the male radio button- ")
print("Male",male.is_selected()) # true
print("Female",female.is_selected()) # false

female.click()
print("after clicking on the female radio button- ")
print("Male",male.is_selected())  # false
print("Female",female.is_selected())  # true


# navigation commands forward() back() refresh()
driver.get("https://www.youtube.com/")
time.sleep(2)
driver.back()
time.sleep(2)

driver.forward()
driver.refresh()

# browser commands close() quit()

# element = driver.find_element(By.XPATH, "//a[normalize-space()='nopCommerce']")
# element.click()

# driver.close()
# closes one tab, which is focused. doesn't kill the process just closes the window
# time.sleep(5)

driver.quit()
# closes all the tabs in the webpage, kills the process regarding chrome driver so all windows closes
time.sleep(5)
