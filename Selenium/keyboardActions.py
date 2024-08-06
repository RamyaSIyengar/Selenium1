# ctrl + A
# ctrl + c
# tab
# ctrl + v
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://text-compare.com/')

input1 = driver.find_element(By.ID, "inputText1")
input2 = driver.find_element(By.ID, "inputText2")

input1.send_keys("Welcome to Selenium")

act = ActionChains(driver)

# input1 => ctrl A

# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)


