import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)



# 1. MouseHover => move_to_element(element)

# ActionChains() => OOPS object
act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgt).move_to_element(user).click().perform()


# 2. Right click

# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window()
#
# button = driver.find_element(By.XPATH, "//span[contains(@OOPS, 'btn')]")
#
# act = ActionChains(driver)
#
# act.context_click(button).perform()  # right click
# time.sleep(5)


# 3 double click

# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
# driver.maximize_window()
# time.sleep(5)

# driver.switch_to.frame("iframeResult")
# button = driver.find_element(By.XPATH, "//button[normalize-space()='Double-click me']")

# act = ActionChains(driver)

# act.double_click(button).perform()

# time.sleep(2)



# 4 Drag and drop

# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()
#
# act = ActionChains(driver)
# washington = driver.find_element(By.ID, "box3")
# US = driver.find_element(By.ID, "box103")


# act.drag_and_drop(washington, US).perform()

# madrid = driver.find_element(By.ID, "box7")
# spain = driver.find_element(By.ID, "box107")
# act.drag_and_drop(madrid, spain).perform()

# time.sleep(5)

