from QA.web_tests.account_manager.login.page import AccountManagerLoginPage
from QA.web_tests.account_manager.login.locators import AccountManagerLoginLocators
from QA.web_tests.account_manager.login.labels import AccountManagerLoginLabels
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class TestLogin(unittest.TestCase):

    desired_cap = {
     'browser': 'Chrome',
     'browser_version': '67.0',
     'os': 'OS X',
     'os_version': 'High Sierra',
     'resolution': '1024x768'
    }

    homepage = 'https://my-staging.earnup.com'

    driver = webdriver.Chrome()

    page = AccountManagerLoginPage()
    locators = AccountManagerLoginLocators()

    def test_tc_login_05(self):
        test_name = "Test Case Login 05 - Login with valid email/password"
        print("Running Test: %s" % test_name)
        self.username = 'ufbaseg@mailinator.com'
        self.password = 'earnup1!'
        self.driver.get(self.homepage)
        self.page.login(self.driver, self.username, self.password)
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
