import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

# 1. find_element
#returns webelement
# a) locator matching single web element
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("Apple macbook")

# b) locator matching multiple web elements
elements = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(elements.text)

# c) if locator doesnt able to find element -> it throws noSuchElementException
# elements = driver.find_element(By.LINK_TEXT, "log")
# Message: no such element: Unable to locate element: {"method":"link text","selector":"log"}


# 2. find_elements - returns multiple web Elements
# a) find_elements always returns a list. if you want to access the web element, you hv select by index
elements1 = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(elements1))  #1
elements1[0].send_keys("13 lite")

# b) locators matching multiple elements
elementss = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(elementss))  #23
# print(elementss[1].text)
for element in elementss:
    print(element.text)

# c) if locator doesnt able to find elements -> it doesn't throws noSuchElementException
elements2 = driver.find_elements(By.LINK_TEXT, "log")
print("elements found", len(elements2))  # 0

# text vs getattribute
# when you send keys from here, before that there are no inner text in input, to fetch that value use get_attribute

inputBox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("using text - ",inputBox.text)
print("using get_attribute -",inputBox.get_attribute('value'))
