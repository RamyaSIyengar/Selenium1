
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# static web table

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1 Count No of rows and columns in the table

noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
# NoOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

noOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))

print("No Of rows", noOfRows)
print("No Of rows", noOfColumns)

# 2  Read specific row and column from the table

row5Column1 = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]")
print(row5Column1.text)

# 3 Read all rows and columns
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")

# String Interpolation in XPath: You cannot directly insert the variables i and j
# inside the XPath.You need to use string formatting to properly construct the XPath.f"{}


# for i in range(2, noOfRows + 1):
#     for j in range(1, noOfColumns + 1):
#         # print(f"Row {i}, Column {j}")
#         xpath = f"//table[@name='BookTable']/tbody/tr[{i}]/td[{j}]"
#         # xpath = f"//table[@name='BookTable']/tbody/tr['+str(i)+']/td['+str(j)+']"
#         data = driver.find_element(By.XPATH, xpath).text
#         print(data, end='           ')
#     print()

# 4. Read data based on condition (list book name whose author is Mukesh)

for row in range(2, noOfRows+1):
    authorName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[1]").text
        price = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[4]").text
        print(bookName, authorName, price)


