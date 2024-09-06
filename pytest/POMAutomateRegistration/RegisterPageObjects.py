import time

import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException



class RegisterClass:

    # Locators
    txtbox_fname_id = 'input-firstname'
    txtbox_lname_id = 'input-lastname'
    txtbox_email_id = 'input-email'
    txtbox_password_id = 'input-password'
    toggle_checkbox_id = 'input-newsletter'
    toggle_privacyPolicy_name = "agree"
    button_continue_xpath = "//button[normalize-space()='Continue']"

    # constructor
    def __init__(self, driver):
        self.driver = driver



    # actions
    def setfirstname(self, fname):
        self.driver.find_element(By.ID, self.txtbox_fname_id).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.ID, self.txtbox_lname_id).send_keys(lname)

    def setemail(self, email):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    def checksubscribe(self):
        self.driver.find_element(By.ID, self.toggle_checkbox_id).click()

    def agreeprivacy(self, retries=3):
        # privacy_checkbox = self.driver.find_element(By.NAME, self.toggle_privacyPolicy_name)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", privacy_checkbox)
        # privacy_checkbox.click()

        # Ensure the privacy policy checkbox is visible and clickable
        # privacy_checkbox = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, self.toggle_privacyPolicy_name))
        # )
        # privacy_checkbox.click()

        for i in range(retries):
            try:
                self.driver.find_element(By.NAME, self.toggle_privacyPolicy_name).click()
                return
            except ElementClickInterceptedException:
                time.sleep(1)
        raise

    def clickcontinue(self):
        # self.driver.find_element(By.XPATH, self.button_continue_xpath).click()


        # Ensure the continue button is visible and clickable
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_continue_xpath))
        )
        button.click()






