import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service

# serv_obj = Service("")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()
driver.get('https://money.rediff.com/gainers/bse/daily/groupa')
driver.maximize_window()
# self
text_self = driver.find_element(By.XPATH, "//a[contains(text(),'West Coast Paper')]/self::a").text
print(text_self)

# parent
text_parent = driver.find_element(By.XPATH, "//a[contains(text(),'West Coast Paper')]/parent::td").text
print(text_parent)  # West Coast Paper
# if a parent element doesn't hv any text, it will give the self text itself

# child
ancestorChild = driver.find_elements(By.XPATH, "//a[contains(text(), 'West Coast Paper')]/ancestor::tr/child::td")
print(len(ancestorChild))  # 6

# ancestor
ancestor = driver.find_element(By.XPATH, "//a[contains(text(),'West Coast Paper')]/ancestor::tr").text
print(ancestor)  # West Coast Paper A 685.80 738.35 + 7.66 Buy  |  Sell

# descendant

descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'West Coast Paper')]/ancestor::tr/descendant::*")
print(len(descendants)) # 10

# Following
following = driver.find_elements(By.XPATH, "//a[contains(text(), 'West Coast Paper')]/ancestor::tr/following::*")
print(len(following)) # 3505

# Following Sibling - subset of following
followingSibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'West Coast Paper')]/ancestor::tr/following-sibling::*")
print(len(followingSibling))

# preceding
preceding = driver.find_elements(By.XPATH, "//a[contains(text(), 'West Coast Paper')]/ancestor::tr/preceding::*")
print("preceding ", len(preceding))  # 263

# Preceding Sibling
precedingSibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'West Coast Paper')]/ancestor::tr/preceding-sibling::*")
print("preceding siblings ", len(precedingSibling)) # 8


time.sleep(5)
