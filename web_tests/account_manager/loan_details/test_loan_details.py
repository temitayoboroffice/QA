from QA.web_tests.account_manager.login.page import AccountManagerLoginPage
from QA.web_tests.account_manager.login.locators import AccountManagerLoginLocators
from QA.web_tests.account_manager.login.labels import AccountManagerLoginLabels
from QA.web_tests.account_manager.main_page.page import AccountManagerMainPage
from QA.web_tests.account_manager.main_page.locators import AccountManagerMainPageLocators
from QA.web_tests.account_manager.main_page.labels import AccountManagerMainlabels
from QA.web_tests.account_manager.loan_details.page import AccountManagerLoanDetailsPage
from QA.web_tests.account_manager.loan_details.assertions import AccountManagerLoanDetailsAssertions
from QA.web_tests.pay_schedule import PaySchedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestLoanDetails(unittest.TestCase):

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
    main_page = AccountManagerMainPage()
    page = AccountManagerLoanDetailsPage()
    assertions = AccountManagerLoanDetailsAssertions()

    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(10)

    @unittest.skip("skip")
    def test_uf_base_i(self):
        test_name = "User Flow Base-I - Change Single Withdrawal Date"
        print("Running Test: %s" % test_name)
        self.username = 'ufbaseh@mailinator.com'
        self.password = 'earnup1!'
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.main_page.click_loan_panel(self.driver)
        self.page.select_change_single_withdrawal_date(self.driver)
        old_date, new_date = self.page.single_withdrawal_modal.select_first_withdrawal_date_options(self.driver)
        old_bool, new_bool = self.page.single_withdrawal_modal.confirm_date_selections_in_panel(self.driver, old_date, new_date)
        print("Success verifying selected dates: ", old_bool, new_bool)
        print(old_bool, new_bool)
        self.page.single_withdrawal_modal.click_save_changes_button(self.driver)
        self.page.select_change_single_withdrawal_date(self.driver)
        old_bool, new_bool = self.page.single_withdrawal_modal.select_old_new_withdrawal_dates(self.driver,
            new_date, old_date)
        print("Success re-selecting original dates: ", old_bool, new_bool)
        old_bool, new_bool = self.page.single_withdrawal_modal.confirm_date_selections_in_panel(self.driver, old_date, new_date)
        print("Success verifying selected dates: ", old_bool, new_bool)
        self.page.single_withdrawal_modal.click_save_changes_button(self.driver)


    def test_uf_base_h(self):
        test_name = "User Flow Base-H - Change Withdrawal Schedule"
        print("Running Test: %s" % test_name)
        self.username = 'ufbaseh@mailinator.com'
        self.password = 'earnup1!'
        test_schedule = 'Every Other Week'
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.main_page.click_loan_panel(self.driver)
        schedule = PaySchedule(type=test_schedule)
        print ('schedule is: %s' % schedule)
        schedule_types = PaySchedule.schedule_types
        print(schedule_types)
        print('current schedule is: %s' % (self.page.get_current_schedule_from_detail_view(self.driver)))
        self.page.select_change_withdrawal_schedule(self.driver)
        self.page.change_withdrawal_modal.select_pay_schedule(self.driver, schedule.schedule_dict)
        self.page.change_withdrawal_modal.click_modal_next_button(self.driver)
        self.page.change_withdrawal_modal.click_confirm_changes_button(self.driver)
        self.assertions.assert_correct_schedule_in_panel(self.driver, test_schedule)

    def test_uf_base_f(self):
        test_name = "User Flow Base-F - Edit User Bank Account Info"
        print("Running Test: %s" % test_name)
        self.username = 'ufbasef@mailinator.com'
        self.password = 'earnup1!'
        test_bank_info = {'bank_name':'Iron Bank Ltd',
         'account_type':'Savings',
         'routing_number':'114910222',
         'account_number':'123456789'}
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.main_page.click_loan_panel(self.driver)
        self.page.select_edit_bank_account(self.driver)
        self.page.edit_bank_info_modal.select_add_new_account_from_dropdown(self.driver)
        self.page.edit_bank_info_modal.click_enter_bank_details_manually(self.driver)
        self.page.edit_bank_info_modal.enter_new_bank_info(self.driver, test_bank_info)
        self.page.select_edit_bank_account(self.driver)
        returned_info = self.page.edit_bank_info_modal.get_bank_info(self.driver)
        print ("Saved Bank Account Information:\n", returned_info)
        for key in test_bank_info.keys():
            assert returned_info[key]==test_bank_info[key], "There are discrepancies in information submitted"+\
            " and information saved for key: %s\n Expected: %s \nFound: %s " % (key, returned_info[key], test_bank_info[key])
        self.page.edit_bank_info_modal.click_edit_new_bank_info_confirm_button(self.driver)


    @unittest.skip("skip")
    def test_get_edit_bank_account_info(self):
        test_name = "User Flow Base-F - B - Getting User Bank Account Info"
        print("Running Test: %s" % test_name)
        self.username = 'ufbasef@mailinator.com'
        self.password = 'earnup1!'
        test_bank_info = {'bank_name':'Iron Bank Ltd',
         'account_type':'Savings',
         'routing_number':'114910222',
         'account_number':'123456789'}
        self.driver.get(self.homepage)
        self.login_page.login(self.driver, self.username, self.password)
        self.main_page.click_loan_panel(self.driver)
        self.page.select_edit_bank_account(self.driver)
        my_bank_info = self.page.edit_bank_info_modal.get_bank_info(self.driver)
        print("bank info is: \n", my_bank_info)





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
