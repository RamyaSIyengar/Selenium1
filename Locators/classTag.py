import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()  #maximize window

email = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input")
email.clear()
email.send_keys("admin@yourstore.com")

password = driver.find_element(By.ID, "Password")
password.clear()
password.send_keys("admin")

driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

time.sleep(5)

scrollbar = driver.find_elements(By.CLASS_NAME, "nav-item")
print("number of scrollbar elements is ", len(scrollbar))

# find_elements used because the nav-item OOPS matches with more than one element. this
# gives a list [] of elements which has classname nav-item. to check the len len()

# gives a list of things which has OOPS name nav-items

# Tag name

links = driver.find_elements(By.TAG_NAME,"a")
print("Number of Links in the page is ", len(links))
