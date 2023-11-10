from selenium import webdriver
from selenium.webdriver.common.by import By

class AddNewUser:
    textbox_Username_xpath = "//input[@name='username']"
    textbox_Password_name = "password"
    button_Login_xpath = "//button[@type='submit']"
    click_PIM_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    click_add_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    textbox_firstname_xpath = "//input[@class='oxd-input oxd-input--active orangehrm-firstname']"
    textbox_middlename_xpath = "//input[@class='oxd-input oxd-input--active orangehrm-middlename']"
    textbox_lastname_xpath = "//input[@class='oxd-input oxd-input--active orangehrm-lastname']"
    textbox_employeeid_xpath ="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    click_savebutton_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

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

    def clickAdd(self):
        self.driver.find_element(By.XPATH,self.click_add_xpath).click()

    def setFirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.textbox_firstname_xpath).send_keys(firstname)

    def setMiddlename(self,middlename):
        self.driver.find_element(By.XPATH, self.textbox_middlename_xpath).send_keys(middlename)

    def setLastname(self,lastname):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(lastname)

    def setEmployeeID(self,empid):
        self.driver.find_element(By.XPATH, self.textbox_employeeid_xpath).send_keys(empid)

    def click_Save(self):
        self.driver.find_element(By.XPATH,self.click_savebutton_xpath).click()







