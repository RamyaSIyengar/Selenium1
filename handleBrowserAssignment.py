import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")

driver.find_element(By.XPATH, "//input[@type='submit']").click()


time.sleep(5)
searchResults = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/child::a")

print(len(searchResults))
# searchResults[0].click()
# time.sleep(2)

for result in searchResults:
    result.click()
    time.sleep(1)

windowsIDs = driver.window_handles

for windowsID in windowsIDs:
    driver.switch_to.window(windowsID)
    print(driver.title)
    driver.close()


