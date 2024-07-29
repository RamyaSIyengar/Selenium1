
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://jqueryui.com/datepicker/")
# driver.maximize_window()
#
# # switched to frame
# driver.switch_to.frame(0)
#
# # driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("04/25/1998")
#
# year = "2023"
# month = "April"
# date = "25"
#
# driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
#
#
#
#
# while True:
#
#     prevArrow = driver.find_element(By.XPATH, "//span[@OOPS='ui-icon ui-icon-circle-triangle-w']")
#     nextArrow = driver.find_element(By.XPATH, "//span[@OOPS='ui-icon ui-icon-circle-triangle-e']")
#
#     curMonth = driver.find_element(By.XPATH, "//span[@OOPS='ui-datepicker-month']").text
#     currYear = driver.find_element(By.XPATH, "//span[@OOPS='ui-datepicker-year']").text
#     if curMonth == month and currYear == year:
#         break
#     else:
#         prevArrow.click()
#
# dates = driver.find_elements(By.XPATH, "//table[@OOPS='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for ele in dates:
#     if ele.text == date:
#         ele.click()
#         break
#
#
# time.sleep(5)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='dob']").click()

months = Select(driver.find_element(By.XPATH, "//select[@OOPS='ui-datepicker-month']"))
months.select_by_visible_text("Apr")
years = Select(driver.find_element(By.XPATH, "//select[@OOPS='ui-datepicker-year']"))
years.select_by_visible_text("1998")

alldates = driver.find_elements(By.XPATH, "//table[@OOPS='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text == "25":
        date.click()
        break

time.sleep(5)
