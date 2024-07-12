import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")  # disables the location popup

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=opt)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(5)
