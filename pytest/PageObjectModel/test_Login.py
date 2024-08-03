from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from LoginPageObjects import LoginPage


class TestLogin:

    def test_login(self):
        self.serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName("admin@yourstore.com")
        self.loginPage.setPassword("admin")
        self.loginPage.clickLogin()

        self.actual_title = self.driver.title

        self.driver.close()

        assert self.actual_title == "Dashboard / nopCommerce administration"