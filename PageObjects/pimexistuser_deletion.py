from selenium import webdriver
from selenium.webdriver.common.by import By

class ExistingUser_del:
    textbox_Username_xpath = "//input[@name='username']"
    textbox_Password_name = "password"
    button_Login_xpath = "//button[@type='submit']"
    click_PIM_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    click_delbtn_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_Login_xpath).click()

    def clickPIM(self):
        PIM_btn = self.driver.find_element(By.XPATH,self.click_PIM_xpath)
        PIM_btn.click()

    def delbtnclick(self):
        self.driver.find_element(By.XPATH,self.click_delbtn_xpath).click()







