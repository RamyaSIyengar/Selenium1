import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()

dropDown_element = driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
dropDown_select = Select(dropDown_element)

# 3 ways of selecting from dropdown options using builtin methods - by visible text, value, index
dropDown_select.select_by_visible_text("India")
dropDown_select.select_by_value("UGA")
dropDown_select.select_by_index(20)

# capture all options and print them
allCountry = dropDown_select.options
# print("Number of countries in the dropdown", len(allCountry))

# for country in allCountry:
#     print(country.text)


# without using builtin method, select from dropDown
for country in allCountry:
    if country.text == "Uruguay":
        country.click()
        break


# without using Select class, getting options
allOptions = driver.find_elements(By.XPATH, "//div[@id='post-2646']//div[2]//div//div//div//p//select//option")
print(len(allOptions))

time.sleep(5)
