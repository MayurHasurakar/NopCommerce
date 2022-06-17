
class LoginPage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath ="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    #"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    #//input[@value='Log in']
    link_logout_linktext = "Logout"
    #textbox_username_id = "txtUsername"
    #textbox_password_id = "txtPassword"
    #button_login_xpath = "//*[@id='btnLogin']"
    button_login_xpath1 = "//*[@id='navbarText']/ul/li[3]/a"
    button_login_xpath2 = "//*[@id='welcome-menu']/ul/li[3]/a"

    link_logout_linktext1 = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout2(self):
        self.driver.find_element_by_xpath(self.button_login_xpath1).click()
        #self.driver.find_element_by_xpath(self.button_login_xpath2).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext1).click()