from selenium import webdriver
from selenium.webdriver.common.by import By

class ExistingUser:
    textbox_Username_xpath = "//input[@name='username']"
    textbox_Password_name = "password"
    button_Login_xpath = "//button[@type='submit']"
    click_PIM_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    click_editbtn_xpath = "//button[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-pencil-fill']"
    textbox_nickname_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input"
    click_save_xpath = "//button[@type='submit'][1]"

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

    def editbtn_click(self):
        self.driver.find_element(By.XPATH,self.click_editbtn_xpath).click()

    def clear_nickname(self):
        self.driver.find_element(By.XPATH,self.textbox_nickname_xpath).clear()
    def setNickname(self,nickname):
        self.driver.find_element(By.XPATH, self.textbox_nickname_xpath).send_keys(nickname)

    def click_Save(self):
        self.driver.find_element(By.XPATH,self.click_save_xpath).click()







