# wait commands

# 1. implicit wait
# 2. explicit wait

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# 1. implicit wait
# driver.implicitly_wait(15) #seconds
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# searchBar = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
# searchBar.send_keys("selenium")
# searchBar.submit()
#
# driver.find_element(By.XPATH, "//h3[text() = 'Selenium']").click()
#
# driver.quit()


# 2. explicit wait
myWait = WebDriverWait(driver, 10, ignored_exceptions=
                               [NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException,
                               Exception], poll_frequency=2)  # explicit wait declaration
driver.get("https://www.google.com/")
driver.maximize_window()

searchBar = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
searchBar.send_keys("selenium")
searchBar.submit()

searchLink = myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchLink.click()

driver.quit()
