# switch_to.frame(name of the frame) => selenium 4
# switch_to.frame(id of the frame)
# switch_to.frame(webelement)
# switch_to.frame(0)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)



# 1 two Frames in main page
# driver.get("https://practice-automation.com/iframes/")
# driver.maximize_window()
#
# time.sleep(3)
#
#
# driver.switch_to.frame("bottom-iframe")
# driver.find_element(By.XPATH, "//a[@class='selenium-button selenium-webdriver text-uppercase fw-bold']").click()
# time.sleep(5)
#
# driver.switch_to.default_content()  # go back to main content from frame
#
# driver.switch_to.frame("top-iframe")
# driver.find_element(By.XPATH, "//a[@href='/docs/intro']").click()
# time.sleep(5)



# 2  Frame inside a frame

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()


driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

time.sleep(5)

outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)

innerFrame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")

driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Hii")

time.sleep(5)




