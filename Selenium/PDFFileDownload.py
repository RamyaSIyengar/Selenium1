import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    #download files in desired location
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}

    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
    #download files in desired location
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True} # HAVE OPEN BUG
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
    #settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList",2) #0-desktop 1-downloads folder 2- Desired loc
    ops.set_preference("browser.download.dir",location)
    ops.set_preference("pdfjs.disabled",True) # for pdf
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver

#Automation code
#driver=chrome_setup()
#driver=edge_setup()
driver=firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
