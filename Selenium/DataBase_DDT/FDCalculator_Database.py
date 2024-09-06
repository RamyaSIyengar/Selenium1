import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import mysql

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.implicitly_wait(10)
driver.maximize_window()

try:
    connection = mysql.connector.connect(host="localhost", port=3307, user="root", passwd="root",
                                         database="mydb")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM caldata")
    for row in cursor:
        # print(row[0], row[1], row[2], row[3], row[4], row[5])
        # reading data from database
        principle = row[0]
        interest = row[1]
        period1 = row[2]
        period2 = row[3]
        freq = row[4]
        expected_maturity = row[5]

        # passing data to application
        driver.find_element(By.ID, 'principal').send_keys(principle)
        driver.find_element(By.ID, 'interest').send_keys(interest)
        driver.find_element(By.ID, 'tenure').send_keys(period1)
        per2 = driver.find_element(By.ID, 'tenurePeriod')
        period2_select = Select(per2)
        period2_select.select_by_visible_text(period2)
        frequency = driver.find_element(By.ID, 'frequency')
        frequency_select = Select(frequency)
        frequency_select.select_by_visible_text(freq)

        calc_button = driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[1]")
        driver.execute_script("arguments[0].click();", calc_button)

        # act = ActionChains(driver)
        # act.move_to_element(calc_button).click().perform()

        actual_result = driver.find_element(By.XPATH, "//span[@class='gL_27']").text

        # validation
        print(float(actual_result), float(expected_maturity))
        if float(actual_result) == float(expected_maturity):
            print("Test Passed")
        else:
            print("Test Failed")
        clear = driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[2]//img")
        driver.execute_script("arguments[0].click();", clear)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(clear)).click()
        # clear.click()
    connection.close()
except:
    print("Connection failed")
driver.close()

