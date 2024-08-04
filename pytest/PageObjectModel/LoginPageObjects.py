from selenium import webdriver
from selenium.webdriver.common.by import By


#  we have to keep only the page elements which are belongs to only one single page on your application.
class LoginPage:

    # Locators
    txtbox_username_id = "Email"   # variable name - txtbox-element, username-what kind of element, id-locator
    txtbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions   => find elements using locators above
    def setUserName(self, username):
        usernametxt = self.driver.find_element(By.ID, self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)
    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

