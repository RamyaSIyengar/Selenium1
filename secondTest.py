import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
# driver.implicitly_wait(10)

email = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input")
email.clear()
email.send_keys("admin@yourstore.com")


driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# //*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button

actual_title = driver.title
expected_title = "Dashboard / nopCommerce administration"

if actual_title == expected_title:
    print("Login Test passed")
else:
    print("Login test failed")

driver.close()