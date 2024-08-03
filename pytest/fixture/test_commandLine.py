from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCLI:

    def test_Login(self, setup):
        # print(setup)
        self.driver = setup

        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
        except NoSuchElementException as e:
            print(f"Page did not load properly {e}")

        self.login_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.login_username.send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
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