import random
import string
import pytest

from selenium import webdriver
from utilitties.readproperties import ReadConfig
from  utilitties.customLogger import  LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage

class Test_003_AddCustomer:

    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AddCustomer(self, setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login Successfull *********************")

        self.logger.info("******************* Starting add customer test *********************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.addCust.clickOnAddnew()

        self.logger.info("******************* Providing customer info *********************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("abc@123")
        self.addCust.setFirstName("maddy")
        self.addCust.setLastName("h")
        self.addCust.setGender("Male")
        self.addCust.setDob("11/11/2011")
        self.addCust.setCompanyName("Maddss")
        #self.addCust.setNewsletterSubscription("Test store 2")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 1")
        self.addCust.setAdminContent("for test purpose")

        self.addCust.clickOnSave()

        self.logger.info("*******************saving customer info *********************")

        self.logger.info("******************* ADD customer validtaion started *********************")

        self.msg =self.driver.find_element_by_tag_name('body').text
        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True
            self.logger.info("******************* Customer added succesfully *********************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddCustomer.png")
            self.logger.info("******************* Add customer test failed *********************")
            assert  False

        self.driver.close()
        self.logger.info("******************* Add Customer Test end *********************")






def random_generator(size=8 , chars = string.ascii_lowercase + string.digits):
    return(''.join(random.choice(chars) for x in range(size)))














