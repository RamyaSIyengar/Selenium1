from selenium import webdriver
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

location = os.getcwd() + "\\handlefilepdf"
print(location)

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

    # download in desired location
    preferences = {
        "download.default_directory": location,
        "profile.default_content_settings.popups": 0,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driverr = webdriver.Chrome(service=serv_obj, options=ops)
    return driverr

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
    # download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driverr = webdriver.Edge(service=serv_obj, options=ops)
    return driverr


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe")
    # settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0-desktop 1-downloads folder 2- Desired loc
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


"""
ops = webdriver.FirefoxOptions(): This creates a new instance of Firefox options, allowing us to customize the browser settings.
ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword"): This sets a preference to automatically download Microsoft Word files (application/msword) without asking.
ops.set_preference("browser.download.manager.showWhenStarting", False): This disables the download manager popup when starting a download.
ops.set_preference("browser.download.folderList", 2): This sets the download location to a custom directory (2). Other options are 0 for the desktop and 1 for the default downloads folder.
ops.set_preference("browser.download.dir", location): This specifies the directory where downloaded files will be saved, using the location parameter passed to the function.
"""


driver = chrome_setup()
# driver = edge_setup()
# driver = firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
wait = WebDriverWait(driver, 10)
download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[5]/a[1]")))
download_button.click()
driver.save_screenshot(os.getcwd() + "\\filedownload.png")

# download is not working
