from QA.web_tests.account_manager.login.page import AccountManagerLoginPage
from QA.web_tests.account_manager.login.locators import AccountManagerLoginLocators
from QA.web_tests.account_manager.login.labels import AccountManagerLoginLabels
from QA.web_tests.account_manager.main_page.page import AccountManagerMainPage
from QA.web_tests.account_manager.main_page.locators import AccountManagerMainPageLocators
from QA.web_tests.account_manager.main_page.labels import AccountManagerMainlabels
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class TestMainPage(unittest.TestCase):

    desired_cap = {
     'browser': 'Chrome',
     'browser_version': '67.0',
     'os': 'OS X',
     'os_version': 'High Sierra',
     'resolution': '1024x768'
    }

    homepage = 'https://my-staging.earnup.com'

    #driver = webdriver.Chrome()

    login_page = AccountManagerLoginPage()
    login_locators = AccountManagerLoginLocators()
    page = AccountManagerMainPage()

    '''test data'''
    username = 'ufbaseg@mailinator.com'
    password = 'earnup1!'
    alternate_username = 'ufbaseg2@mailinator.com'


    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_test_uf_base_g_a(self):
        test_name = "User Flow Base-G - Edit User's email"
        print("Running Test: %s" % test_name)
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.page.select_edit_my_info_button(self.driver)
        print("Email: ", self.page.get_email_text(self.driver))
        #print("Phone: ", self.page.get_primary_phone_text(self.driver))
        self.page.set_email_text(self.driver, self.alternate_username)
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        email_text = self.page.get_email_text(self.driver)
        print("Email: ", self.page.get_email_text(self.driver))
        self.page.set_email_text(self.driver, self.username)
        print("Email: ", self.page.get_email_text(self.driver))
        self.page.click_confirm_button(self.driver)
        if email_text != self.alternate_username:
            assert False, "Fields changes were not retained.\nExpected: %s\nFound: %s" % (self.alternate_username,
            email_text)

    def test_uf_base_g_b(self):
        test_name = "User Flow Base-G - Edit User's Primary Phone"
        print("Running Test: %s" % test_name)
        self.phone_number = '(617) 222-1111'
        self.alternate_phone_number = ['(212) 444-4444', '(212) 555-5555']
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.page.select_edit_my_info_button(self.driver)
        phone_text = self.page.get_primary_phone_text(self.driver)
        print("\nCurrent Primary Phone #: ", phone_text)
        test_alternate = ''
        if phone_text == self.alternate_phone_number[0]:
            test_alternate = self.alternate_phone_number[1]
        else:
            test_alternate = self.alternate_phone_number[0]
        print("Attempting to change Primary Phone # to ", test_alternate)
        self.page.set_primary_phone_text(self.driver, test_alternate)
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        print("Verifying changes")
        phone_text = self.page.get_primary_phone_text(self.driver)
        print("New Phone: ", phone_text)
        assert phone_text == test_alternate, "Edited Phone number was not saved\
            \nExpected: %s\nFound: %s" % (test_alternate,
            phone_text)
        print("Attempting to reset Primary Phone # to ", self.phone_number)
        self.page.set_primary_phone_text(self.driver, self.phone_number)
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        print("Verifying changes")
        phone_text = self.page.get_primary_phone_text(self.driver)
        print("Phone: ", phone_text)
        self.page.click_confirm_button(self.driver)
        if phone_text != self.phone_number:
            assert False, "Primary Phone Number was not retained.\nExpected: %s\nFound: %s" % (self.phone_number,
            phone_text)

    def test_uf_base_g_c(self):
        test_name = "User Flow Base-G - Edit User's Secondary Phone"
        print("Running Test: %s" % test_name)
        self.phone_number = '(617) 423-1233'
        self.alternate_phone_number = ['(212) 777-7777', '(212) 888-8888']
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.page.select_edit_my_info_button(self.driver)
        phone_text = self.page.get_secondary_phone_text(self.driver)
        print("\nCurrent secondary Phone #: ", phone_text)
        test_alternate = ''
        if phone_text == self.alternate_phone_number[0]:
            test_alternate = self.alternate_phone_number[1]
        else:
            test_alternate = self.alternate_phone_number[0]
        print("Attempting to change secondary Phone # to ", test_alternate)
        self.page.set_secondary_phone_text(self.driver, test_alternate)
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        phone_text = self.page.get_secondary_phone_text(self.driver)
        print("Verifying changes")
        print("New Phone: ", phone_text)
        assert phone_text == test_alternate, "Edited Phone number was not saved\
            \nExpected: %s\nFound: %s" % (test_alternate,
            phone_text)
        print("Attempting to reset secondary Phone # to ", self.phone_number)
        self.page.set_secondary_phone_text(self.driver, self.phone_number)
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        phone_text = self.page.get_secondary_phone_text(self.driver)
        print("Verifying changes")
        print("Phone: ", phone_text)
        self.page.click_confirm_button(self.driver)
        if phone_text != self.phone_number:
            assert False, "Secondary Phone Number was not retained.\nExpected: %s\nFound: %s" % (self.phone_number,
            phone_text)

    def test_uf_base_g_d(self):
        test_name = "User Flow Base-G - Edit User's Address"
        print("Running Test: %s" % test_name)
        self.username = 'ufbaseg@mailinator.com'
        self.password = 'earnup1!'
        self.address = '137 Ferry St, Everett MA 02149'
        self.alternate_address = ['40 Princeton Street Apt 2, Boston MA 02128',
            '20 Darling Street, Boston MA 02120']
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.page.select_edit_my_info_button(self.driver)
        address_text = self.page.get_address_text(self.driver)
        #print("Email: ", self.page.get_email_text(self.driver))
        print("\nCurrent Address: ", address_text)
        test_alternate = ''
        if address_text == self.alternate_address[0]:
            test_alternate = self.alternate_address[1]
        else:
            test_alternate = self.alternate_address[0]
        print("Attempting to change Address to ", test_alternate)
        self.page.set_address_text(self.driver, test_alternate)
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        address_text = self.page.get_address_text(self.driver)
        print("Verifying changes")
        print("New Address: ", address_text)
        assert test_alternate in address_text, "Edited Address was not saved\
            \nExpected: %s\nFound: %s" % (test_alternate,
            address_text)
        print("Attempting to reset Address to ", self.address)
        self.page.set_address_text(self.driver, self.address)
        print("Address: ", self.page.get_address_text(self.driver))
        self.page.click_confirm_button(self.driver)
        self.page.select_edit_my_info_button(self.driver)
        print("Verifying changes")
        address_text = self.page.get_address_text(self.driver)
        if self.alternate_address not in address_text:
            assert False, "Address was not retained.\nExpected: %s\nFound: %s" % (self.alternate_address,
            address_text)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
