# internal links
# external links
# broken links

import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")

# 1 click on a link
# driver.find_element(By.LINK_TEXT, "Comparison Table.").click()
# time.sleep(5)

# 2 Find no of links in a page
# links = driver.find_elements(By.TAG_NAME, "a")

# approach 2
# links1 = driver.find_elements(By.XPATH, "//a")
# print("total number of links:", len(links1))

# 3 print all the links
# for link in links1:
#     print(link.text)


# Broken Links
# request model is a pre requisites => File -> Settings -> ProjectInterpreter -> + -> requests
import requests as requests

allLinks = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in allLinks:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)  # it can throw some network error, so use try except block
    except:
        None
    if res.status_code >= 400:
        print(url, "Broken Link")
        count += 1
    else:
        print(url, "Valid Url")


print(count, "no of broken Links in this page")
# 40 no of invalid url in this page

