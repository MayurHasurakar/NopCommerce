import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilitties.readproperties import ReadConfig
from utilitties.customLogger import LogGen
import time

class Test_001_Login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homepage(self, setup):

        self.logger.info("*************** Test_001_Login *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********************* Test home page Passed  *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePage.png")
            self.driver.close()
            self.logger.error("********************* Test home page Failed   *****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********************* Test Login    *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        #self.driver.back()
        #self.lp.clickLogout()
        #time.sleep(2)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********************* Test  Login passed  *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********************* Test  Login Failed  *****************")
            assert False
