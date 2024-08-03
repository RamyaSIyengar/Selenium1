import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    # print("Launching browser")   # stage1

    if browser == 'chrome':
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)

    elif browser == 'edge':
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)

    elif browser == 'firefox':
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe")
        driver = webdriver.Edge(service=serv_obj)

    return driver


def pytest_addoption(parser):     # this will get the value for the browser from the Command line prompt
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):      # this will return the Browser value to setup method
    return request.config.getoption("--browser")


# customizing HTML report
# it is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'Ramya'


# it is a hook for delete/Modify environment info in HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# command to run - pytest -v -s .\pytest\fixture\test_commandLine.py --browser edge/chrome/firefox


