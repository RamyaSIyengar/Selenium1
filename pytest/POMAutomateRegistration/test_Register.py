import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from RegisterPageObjects import RegisterClass


class TestRegister:

    def test_register(self):
        self.serv_obj = Service('C:\Drivers\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get('https://demo.opencart.com/en-gb?route=account/register')
        self.driver.maximize_window()

        self.reg = RegisterClass(self.driver)

        self.reg.setfirstname('Ramya')
        self.reg.setlastname('Iyengar')
        self.reg.setemail('ramyaiyen23@gmail.com')
        self.reg.setpassword('admin123')
        # self.reg.checksubscribe()
        self.reg.agreeprivacy()
        self.reg.clickcontinue()
        time.sleep(10)

        # accCreated = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']").text
        # self.driver.close()
        #
        # assert accCreated == "Your Account Has Been Created!"
