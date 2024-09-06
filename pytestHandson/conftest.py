import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope="function", autouse=True)
def setup(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




# @pytest.fixture(scope='class')
# def setup(request):
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     request.cls.driver = driver
#
#     yield driver
#     driver.quit()