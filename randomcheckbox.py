import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import random



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()
driver.implicitly_wait(10)


choice1 = random.randrange(1,4)
choice2 = random.randrange(1,4)

for i in [choice1, choice2]:
    checkbox = driver.find_element(By.XPATH, f"//div[4][@class='display']/input[{i}]")
    checkbox.click()


time.sleep(5)