from selenium import webdriver
from QA.web_tests.account_manager.login.page import AccountManagerLoginPage
from QA.web_tests.account_manager.login.locators import AccountManagerLoginLocators
from QA.web_tests.account_manager.login.labels import AccountManagerLoginLabels
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

page = AccountManagerLoginPage()
locators = AccountManagerLoginLocators()

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '67.0',
 'os': 'OS X',
 'os_version': 'High Sierra',
 'resolution': '1024x768'
}

driver = webdriver.Chrome()

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = page.find_name(self."q")
elem.send_keys("BrowserStack")
elem.submit()
print (driver.title)
driver.quit()
