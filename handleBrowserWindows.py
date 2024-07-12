import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

windowID = driver.current_window_handle
print(windowID)  #D42856B9288C5780DDEBCEBA7428EA2E

time.sleep(5)

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)

windowsIDs = driver.window_handles  # to get windowId of all the windows so that we can switch
print(windowsIDs)

# Approach 1
# parentWindow = windowsIDs[0]
# childWindow = windowsIDs[1]
#
# # switch from one window to another
# driver.switch_to.window(childWindow)
# print("title of the child window", driver.title)  # Human Resources Management Software | OrangeHRM
#
# time.sleep(5)
#
# driver.switch_to.window(parentWindow)
# print("title of the parent window", driver.title)  # OrangeHRM

# Approach 2
for win in windowsIDs:
    driver.switch_to.window(win)
    print(driver.title)

# close specific window
for win in windowsIDs:
    driver.switch_to.window(win)
    if driver.title == "OrangeHRM" or driver.title == "Human Resources Management Software | OrangeHRM":
        driver.close()

time.sleep(5)