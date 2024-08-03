import time

import pytest
from selenium import webdriver
from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClass:

    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
        except WebDriverException as e:
            pytest.fail(f"Failed to load the website: {e}")

        self.login_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        self.login_username.send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_edge(self):
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.serv_obj)
        # Use explicit wait to for the login page to be present
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
        except NoSuchElementException:
            pytest.fail("Element not found")
        self.login_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.login_username.send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    # def test_login_firefox(self):
    #     from selenium.webdriver.firefox.service import Service
    #     self.serv_obj = Service("C:\Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe")
    #     self.driver = webdriver.Firefox(service=self.serv_obj)
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element(By.NAME, "username").send_keys("Admin")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     assert self.driver.title == "OrangeHRM"
    #     self.driver.quit()





# pytest -v -s -n=2 .\pytest\test_parallel.py