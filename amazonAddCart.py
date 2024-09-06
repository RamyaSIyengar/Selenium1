import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Use WebDriverWait for synchronization
wait = WebDriverWait(driver, 10)

# Search for the phone
input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_2SmNnR']/input")))
input_field.send_keys("phone")
input_field.send_keys(Keys.ENTER)

# Click on the first product
frstprdt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='DOjaWF gdgoEp']/div[2]")))
frstprdt.click()

# Switch to the new window
windowsIDs = driver.window_handles
parentWindow = windowsIDs[0]
childWindow = windowsIDs[1]
driver.switch_to.window(childWindow)

# Scroll into view and click "Add to Cart"
addToCartBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")))
driver.execute_script("arguments[0].scrollIntoView(true);", addToCartBtn)
addToCartBtn.click()

# Wait for price details to be visible and assert
pricedetails = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='kQCHPX']/span")))
print(pricedetails.text)
assert "PRICE DETAILS" in pricedetails.text
# Close the driver
driver.quit()
