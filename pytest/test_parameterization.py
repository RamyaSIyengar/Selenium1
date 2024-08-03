import pytest

# Example1
# class TestClass:
#     @pytest.mark.parametrize('num1, num2', [(10, 10), (4, 8), (6, 6), (9, 0)])
#     def test_calculation(self, num1, num2):
#         assert num1 == num2

# Example2

from selenium import webdriver
from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLog:
    @pytest.mark.parametrize('user,pwd',
                             [('Admin', 'admin123'), ('Admin', 'admin'), ('admin', 'admin123'), ('ad', 'ad')])
    def test_login(self, user, pwd):
        self.serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
        except NoSuchElementException as e:
            print(f"Page did not load properly {e}")

        self.login_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.login_username.send_keys(user)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            self.dashboard = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Dashboard']")))
            self.status = self.dashboard.is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False
