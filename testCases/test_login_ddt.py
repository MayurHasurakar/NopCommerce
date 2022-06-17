import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilitties.readproperties import ReadConfig
from utilitties.customLogger import LogGen
from utilitties import XLUtils
import time


class Test_002_DDT_Login:
    base_url = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********************* Test Login    *****************")
        self.logger.info("********************* Test Login DDT    *****************")
        self.driver = setup

        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("no of rows in Excel file is", self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r ,1)
            self.password = XLUtils.readData(self.path,"Sheet1", r , 2)
            self.exp = XLUtils.readData(self.path,"Sheet1", r ,3)
            self.lp.setUsername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clickLogin()
            self.driver.maximize_window()
            time.sleep(2)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass" :
                    self.logger.info("***************** PASSED  1 *****************")
                    self.lp.clickLogout()
                    #self.driver.back()
                    lst_status.append("Pass")


                elif self.exp == "Fail":
                    self.logger.info("***************** Failed 1  *****************")
                    self.lp.clickLogout()
                    #self.driver.back()

                    lst_status.append("Fail")

            elif  act_title != exp_title :
                if self.exp == "Pass":
                   self.logger.info("***************** Failed 2 *****************")
                   lst_status.append("Fail")

                elif self.exp == "Fail" :
                   self.logger.info("***************** Passed 2 *****************")
                   lst_status.append("Pass")
        print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("********DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("******ddt test failed")
            self.driver.close()
            assert False

















