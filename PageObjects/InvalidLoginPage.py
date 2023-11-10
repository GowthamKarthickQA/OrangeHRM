from selenium import webdriver
from selenium.webdriver.common.by import By

class Invalid_Login:
    textbox_Username_xpath = "//input[@name='username']"
    textbox_Password_name = "password"
    button_Login_xpath = "//button[@type='submit']"
    invalidmsg_login_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text'][text()='Invalid credentials']"
    errormsg_invalidlogin_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername_valid(self,username_valid):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(username_valid)

    def setPassword_invalid(self,password_invalid):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(password_invalid)

    def getInvalid_credential_msg(self):
        Invalid_pwd_msg = self.driver.find_element(By.XPATH,self.invalidmsg_login_xpath)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def errormsg_invalidlogin(self):
        credential_msg = self.driver.find_element(By.XPATH,self.errormsg_invalidlogin_xpath)
        print("validation message as ",credential_msg.text)







