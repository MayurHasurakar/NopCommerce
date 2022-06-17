import pytest
from selenium import  webdriver

@pytest.fixture()
def setup(browser):
    if browser == "Chrome" :
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver-v0.31.0-win64\geckodriver.exe")
    return driver


def pytest_addoption(parser):                 #this will get value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
        return request.config.getoption("--browser")

#hook for adding envernomental info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Mayur'

#hook for delete/modify envirnoment info i html report

@pytest.mark.optionalhook
def pytest_metadate(metadata):
   metadata.pop("JAVA_HOME", None)
   metadata.pop("Plugins", None)


