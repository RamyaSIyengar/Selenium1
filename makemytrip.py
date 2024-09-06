
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.makemytrip.com/flight/search?itinerary=BLR-SFO-20/09/2024_SFO-BLR-20/10/2024&tripType=R&paxType=A-1_C-0_I-0&intl=true&cabinClass=E&ccde=IN&lang=eng")
driver.maximize_window()
driver.implicitly_wait(10)


driver.refresh()
airplanes = driver.find_elements(By.XPATH, "//div[@id='listing-id']//div[@class='clusterContent']/div/div[@class=' ']/div/div[2]/div/div/div/div/p[@class='boldFont blackText airlineName']")

print(len(airplanes))
