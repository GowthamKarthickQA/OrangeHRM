import time

from selenium import webdriver
import pytest
from PageObjects.InvalidLoginPage import Invalid_Login
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_login_002:
    baseURL = ReadConfig.getApplicationURL()
    username_valid = ReadConfig.getUsername_valid()
    password_invalid = ReadConfig.getPassword_invalid()

    logger = LogGen.loggen()  # Logger Code

    def test_Invalid_login(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Invalid_Login(self.driver)
        self.lp.setUsername_valid(self.username_valid)
        time.sleep(5)
        self.lp.setPassword_invalid(self.password_invalid)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.errormsg_invalidlogin()
        self.logger.info("*********************** Invalid Credential Message Found.  *************************************")
        self.driver.close()
