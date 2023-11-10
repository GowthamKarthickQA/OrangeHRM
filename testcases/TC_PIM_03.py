import time

from selenium import webdriver
import pytest
from PageObjects.pimexistuser_deletion import ExistingUser_del
from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_ExistUser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger Code

    def test_exist_user(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = ExistingUser_del(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickPIM()
        time.sleep(10)
        self.lp.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(10)
        self.lp.delbtnclick()
        time.sleep(4)
        self.logger.info("*********************** Existing User Deleted Sucessfully *************************************")
        self.driver.close()
