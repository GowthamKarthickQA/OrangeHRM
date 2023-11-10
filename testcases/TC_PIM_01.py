import time

from selenium import webdriver
import pytest
from PageObjects.pimnewuser_add import AddNewUser

from Utilities.customlogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_NewUser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    firstname = ReadConfig.getFirstname()
    middlename = ReadConfig.getMiddlename()
    lastname = ReadConfig.getLastname()
    empid = ReadConfig.getEmp_id()


    logger = LogGen.loggen()  # Logger Code

    def test_new_user(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = AddNewUser(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickPIM()
        time.sleep(10)
        self.lp.clickAdd()
        time.sleep(10)
        self.lp.setFirstname(self.firstname)
        time.sleep(3)
        self.lp.setMiddlename(self.middlename)
        time.sleep(3)
        self.lp.setLastname(self.lastname)
        time.sleep(3)
        self.lp.setEmployeeID(self.empid)
        time.sleep(3)
        self.lp.click_Save()
        time.sleep(5)
        self.logger.info("*********************** New User Added Sucessfully *************************************")
        self.driver.close()
