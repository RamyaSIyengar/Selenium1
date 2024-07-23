import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

# 1 Slider

# driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
# driver.maximize_window()
#
#
# min_slider = driver.find_element(By.XPATH, "//div[@class='price-range-block']//span[1]")
# max_slider = driver.find_element(By.XPATH, "//div[@class='price-range-block']//span[2]")
#
# print("Before, values of min and max sliders ...")
# print(min_slider.location)  # {'x': 59, 'y': 250}
# print(max_slider.location)  # {'x': 510, 'y': 250}
#
# act = ActionChains(driver)
# act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
# act.drag_and_drop_by_offset(max_slider, -10, 0).perform()
#
# print("After values of min and max sliders ...")
# print(min_slider.location)
# print(max_slider.location)

# 2 Scrolling

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

time.sleep(5)

# a] => Sroll down page by pixel

# driver.execute_script("window.scrollBy(0, 3000)", "")
#
# value = driver.execute_script("return window.pageYOffset;")
# print("Num of pixels moved:", value)


# b] => Scroll down page till the element is visible

# Indian_flag = driver.find_element(By.XPATH, "//img[@src='/img/flags/small/tn_in-flag.gif']")
#
# driver.execute_script("arguments[0].scrollIntoView();",Indian_flag)
#
# value = driver.execute_script("return window.pageYOffset;")
# print("Num of pixels moved:", value)  # 4570.66650390625


# Scroll down till end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

value = driver.execute_script("return window.pageYOffset;")
print("Num of pixels moved:", value)  # 11396.6669921875

time.sleep(5)

# Scroll down till top of the page

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

value = driver.execute_script("return window.pageYOffset;")
print("Num of pixels moved:", value)  # 0

time.sleep(5)
