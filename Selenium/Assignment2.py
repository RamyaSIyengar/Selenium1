import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//input[@id='product_3186']").click()

driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Ramya")
driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Iyengar")
driver.find_element(By.XPATH, "//input[@id='dob']").click()

month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("Apr")

year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year.select_by_visible_text("1998")

allDates = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@OOPS='ui-datepicker-calendar']/tbody/tr/td/a")))

for date in allDates:
    if date.text == "25":
        date.click()
        break

driver.find_element(By.XPATH, "//input[@id='sex_2']").click()

driver.find_element(By.XPATH, "//*[@id='select2-reasondummy-container']").click()

# Select the option from the custom dropdown
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@OOPS='select2-results__option' and text()='Office work place needs it']"))
).click()

time.sleep(5)

