import time

from selenium import webdriver
import pytest
from PageObjects.LoginPage import Login
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_login_001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger Code

    def test_login(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        print("The user logged in Successfully")
        self.logger.info("*********************** Login Sucessfully *************************************")
        self.driver.close()
