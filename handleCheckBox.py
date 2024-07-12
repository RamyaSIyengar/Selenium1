import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:\Drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# 1 select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2 Select all the checkboxes
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

# approach 1
# for checkBox in checkBoxes:
#     checkBox.click()

# approach 2
# for i in range(len(checkBoxes)):
#     checkBoxes[i].click()


# 3 Select multiple checkboxes by choice
# for checkBox in checkBoxes:
#     weekName = checkBox.get_attribute('id')
#     if weekName == 'friday' or weekName == 'saturday':
#         checkBox.click()

# 4 Select last two checkboxes
# len of checkboxes - no of checkBoxes to be selected = starting index
# 7-3 = 4, 4 is starting index

# for i in range(len(checkBoxes) - 3, len(checkBoxes)):
#     checkBoxes[i].click()

# 5 Select first two checkboxes

for i in range(len(checkBoxes)):
    if i < 4:
        checkBoxes[i].click()
time.sleep(5)


# 6 clearing all the checkboxes

for i in range(len(checkBoxes)):
    if checkBoxes[i].is_selected():
        checkBoxes[i].click()
# approach 2
for checkBox in checkBoxes:
    if checkBox.is_selected():
        checkBox.click()