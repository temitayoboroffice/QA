from QA.web_tests.core.assertions import Assertions
from QA.web_tests.account_manager.loan_details.locators import AccountManagerLoanDetailsLocators
from QA.web_tests.account_manager.loan_details.labels import AccountManagerLoanDetailsLabels
from QA.web_tests.account_manager.loan_details.change_withdrawal_schedule_modal.page import ChangeWithdrawalScheduleModalPage
from QA.web_tests.account_manager.loan_details.single_withdrawal_modal.page import SingleWithdrawalModalPage
from QA.web_tests.account_manager.loan_details.edit_bank_account_info_modal.page import EditBankAccountInfoModalPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



class AccountManagerLoanDetailsPage(Assertions):

    locators = AccountManagerLoanDetailsLocators()
    labels = AccountManagerLoanDetailsLabels()
    change_withdrawal_modal = ChangeWithdrawalScheduleModalPage()
    single_withdrawal_modal = SingleWithdrawalModalPage()
    edit_bank_info_modal = EditBankAccountInfoModalPage()


    def select_change_withdrawal_schedule(self, tester):
        print("Clicking Change Withdrawal Schedule button")
        assert_text = "Change withdrawal schedule button not found!"
        self.click_xpath(tester, self.locators.LOC_CHANGE_WITHDRAWAL_SCHEDULE_XPATH,
            assert_text=assert_text
        )
        #assert_text = "Change withdrawal modal not found!"
        self.wait_for_modal(tester)

    def select_change_single_withdrawal_date(self, tester):
        print("Clicking Change Single Withdrawal date button")
        assert_text = "Change Single Withdrawal date button not found!"
        self.click_xpath(tester, self.locators.LOC_CHANGE_SINGLE_WITHDRAWAL_DATE_XPATH,
            assert_text=assert_text
        )
        #assert_text = "Change Single Withdrawal date modal not found!"
        self.wait_for_modal(tester)

    def select_make_an_extra_payment(self, tester):
        print("Clicking Make an extra payment button")
        assert_text = "Make an extra payment button not found!"
        self.click_xpath(tester, self.locators.LOC_MAKE_EXTRA_PAYMENT_XPATH,
            assert_text=assert_text
        )
        #assert_text = "Make an extra payment modal not found!"
        self.wait_for_modal(tester)


    def select_edit_bank_account(self, tester):
        print("Clicking Edit Bank Account button")
        assert_text = "Edit Bank Account button not found!"
        self.click_xpath(tester, self.locators.LOC_EDIT_BANK_ACCOUNT_XPATH,
            assert_text=assert_text
        )
        #assert_text = "Edit Bank Account modal not found!"
        self.wait_for_modal(tester)

    def select_suspend_loan_payments(self, tester):
        self.click_xpath(tester, self.locators.LOC_SUSPEND_LOAN_PAYMENTS_XPATH)


    '''This section deals with the Select Single Withdrawal Date Modal'''
    '''


    def select_new_withdrawal_date(self, tester, date_text):
        dates = self.get_list_of_new_withdrawal_dates(tester)
        return self.select_date_by_text(tester, dates, date_text)

    def click_save_changes_button(self, tester):
        self.click_class_and_text(
            tester, self.locators.LOC_SAVE_BUTTON_CLASS,
            self.labels.LBL_CHANGE_SINGLE_WITHDRAWAL_MODAL_SAVE_CHANGES
        )
        self.sleep(2)

    def click_cancel_button(self, tester):
        self.click_class_and_text(
            tester, self.locators.LOC_CANCEL_BUTTON_CLASS,
            self.labels.LBL_CHANGE_SINGLE_WITHDRAWAL_MODAL_CANCEL
        )
        self.sleep(2)

    def select_first_withdrawal_date_options(self, tester):
        self.click_change_withdrawal_drop_down(tester)
        old_date = self.select_first_existing_withdrawal_date(tester)
        self.click_new_withdrawal_drop_down(tester)
        new_date = self.select_first_new_withdrawal_date(tester)
        return (old_date, new_date)

    def select_old_new_withdrawal_dates(self, tester, old_date, new_date):
        self.click_change_withdrawal_drop_down(tester)
        old_bool = self.select_existing_withdrawal_date(tester, old_date)
        self.click_new_withdrawal_drop_down(tester)
        new_bool = self.select_new_withdrawal_date(tester, new_date)
        return(old_bool, new_bool)

    def select_all_the_dates(self, tester):
        self.click_change_withdrawal_drop_down(tester)
        old_bool = self.select_all_existing_withdrawal_dates(tester)
        self.click_new_withdrawal_drop_down(tester)
        new_bool = self.select_all_new_withdrawal_dates(tester)
        return(old_bool, new_bool)

    def compare_date_entries(self, first_text, second_text):
        split_one = first_text.split(' ')
        split_two = second_text.split(' ')
        print(split_one, split_two)
        if split_one[1] == split_two[1] and split_one[2] == split_two[2]:
            if split_one[0] in split_two[0] or split_two[0] in split_one[0]:
                return True
        return False

    def confirm_date_selections_in_panel(self, tester, old_date, new_date):
        old_bool = False
        new_bool = False
        old_panel_date = self.get_date_text_from_panel(tester,
            self.locators.LOC_OLD_DATE_DISPLAY_XPATH)
        new_panel_date = self.get_date_text_from_panel(tester,
            self.locators.LOC_NEW_DATE_DISPLAY_XPATH)
        if self.compare_date_entries(old_date, old_panel_date):
            old_bool = True
        if self.compare_date_entries(new_date, new_panel_date):
            new_bool = True
        print("Panel info:\nOld Date: %s\nNew Date: %s" %(old_panel_date, new_panel_date))
        return (old_bool, new_bool)
        '''

    '''This section deals with the Change Withdrawal Shedule Modal'''

    def get_current_schedule_from_detail_view(self, tester):
        detail = self.find_xpath(tester, self.locators.LOC_PANEL_SCHEDULE_DETAILS_XPATH).text
        if self.labels.LBL_EVERY_OTHER_WEEK_SCHEDULE_TEXT in detail:
            return self.labels.schedule_dict[self.labels.LBL_EVERY_OTHER_WEEK_SCHEDULE_TEXT]
        elif self.labels.LBL_WEEKLY_SCHEDULE_TEXT in detail:
            return self.labels.schedule_dict[self.labels.LBL_WEEKLY_SCHEDULE_TEXT]
        elif self.labels.LBL_TWICE_A_MONTH_SCHEDULE_TEXT in detail:
            return self.labels.schedule_dict[self.labels.LBL_TWICE_A_MONTH_SCHEDULE_TEXT]
        elif self.labels.LBL_ONCE_A_MONTH_SCHEDULE_TEXT in detail:
            return self.labels.schedule_dict[self.labels.LBL_ONCE_A_MONTH_SCHEDULE_TEXT]
        else:
            return None

    def click_pay_freq_schedule_dropdown(self, tester, text_option):
        self.click_id(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_ID)
        self.sleep(2)

    def click_pay_day_dropdown(self, tester):
        self.click_id(tester, self.locators.LOC_PAY_WEEKDAY_SCHEDULE_FORMS_SELECT_ID)
        self.sleep(2)

    def get_list_of_freq_schedule_elements(self, tester):
        list = self.find_xpath(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_WITHDRAWAL_PAY_SCHEDULE_LIST_ITEM_CLASS)

    def get_pay_day_list(self, tester):
        list = self.find_xpath(tester, self.locators.LOC_PAY_WEEKDAY_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_PAY_WEEKDAY_SCHEDULE_LIST_ITEM_CLASS)

    def select_pay_schedule_by_text(self, tester, list_of_schedule_elements, text):
        return self.select_element_from_list_by_text(tester, list_of_schedule_elements, text)

    def select_pay_day_by_text(self, tester, list_of_days, text):
        return self.select_element_from_list_by_text(tester, list_of_days, text)

    def click_biweekly_schedule_dropdown(self, tester):
        self.click_id(tester, self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_FORMS_SELECT_ID)
        self.sleep(2)

    def get_biweekly_pay_dates_list(self, tester):
        list = self.find_xpath(tester, self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_LIST_ITEM_CLASS)

    def select_biweekly_pay_date(self, tester, list_of_dates, text):
        return self.select_element_from_list_by_text(tester, list_of_dates, text)

    def click_bimonthly_schedule_dropdown(self, tester):
        self.click_id(tester, self.locators.LOC_PAY_SEMI_MONTHLY_SCHEDULE_FORMS_SELECT_ID)
        self.sleep(2)

    def get_bimonthly_pay_dates_list(self, tester):
        list = self.find_xpath(tester, self.locators.LOC_PAY_SEMI_MONTHLY_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_PAY_SEMI_MONTHLY_SCHEDULE_ITEM_CLASS)

    def select_bimonthly_pay_date(self, tester, list_of_bimonthly_dates, text):
        return self.select_element_from_list_by_text(tester, list_of_bimonthly_dates, text)

    def click_monthly_schedule_dropdown(self, tester):
        self.click_id(tester, self.locators.LOC_PAY_MONTHLY_SCHEDULE_FORMS_SELECT_ID)
        self.sleep(2)

    def get_month_dates_list(self, tester):
        list = self.find_xpath(tester, self.locators.LOC_PAY_MONTHLY_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_PAY_MONTHLY_SCHEDULE_LIST_ITEM_CLASS)

    def select_date_of_the_month(self, tester, list_of_monthly_dates, text):
        return self.select_element_from_list_by_text(tester, list_of_monthly_dates, text)

    def select_pay_schedule(self, tester, schedule_dict):
        type = schedule_dict['schedule_type']
        self.click_pay_freq_schedule_dropdown(tester, type)
        schedule_list = self.get_list_of_freq_schedule_elements(tester)
        self.select_pay_schedule_by_text(tester, schedule_list, schedule_dict['schedule_type'])
        if type == self.labels.LBL_WEEKLY_SCHEDULE:
            pay_day = schedule_dict['pay_day']
            self.click_pay_day_dropdown(tester)
            pay_day_list = self.get_pay_day_list(tester)
            self.select_pay_day_by_text(tester, pay_day_list, pay_day)
        elif type == self.labels.LBL_EVERY_OTHER_WEEK_SCHEDULE:
            self.select_item_in_dropdown_by_text(tester,
                self.locators.LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_ID,
                self.locators.LOC_PAY_FREQ_SCHEDULE_LIST_XPATH,
                self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_LIST_ITEM_CLASS,
                schedule_dict['pay_day']
            )
            #pay_day = schedule_dict['pay_day']
            #self.click_pay_day_dropdown(tester)
            #pay_day_list = self.get_pay_day_list(tester)
            #self.select_pay_day_by_text(tester, pay_day_list, pay_day)
            #pay_date = schedule_dict['next_pay_day']
            #self.click_biweekly_schedule_dropdown(tester)
            #pay_date_list = self.get_biweekly_pay_dates_list(tester)
            #self.select_biweekly_pay_date(tester, pay_date_list, pay_date)
        elif type == self.labels.LBL_TWICE_A_MONTH_SCHEDULE:
            bimonthly_pay_date = schedule_dict['bimonthly_pay_date']
            self.click_bimonthly_schedule_dropdown(tester)
            bimonthly_pay_date_list = self.get_bimonthly_pay_dates_list(tester)
            self.select_bimonthly_pay_date(tester, bimonthly_pay_date_list, bimonthly_pay_date)
        elif type == self.labels.LBL_MONTHLY_SCHEDULE:
            monthly_date = schedule_dict['monthly_pay_date']
            self.click_monthly_schedule_dropdown(tester)
            dates_list = self.get_month_dates_list(tester)
            self.select_date_of_the_month(tester, dates_list, monthly_date)
        else:
            assert False, "Invalid Schedule Type Selected!"

    def click_modal_next_button(self, tester):
        self.click_xpath(tester, self.locators.LOC_NEXT_BUTTON_XPATH)
        self.sleep(2)

    def click_modal_more_options_button(self, tester):
        self.click_xpath(tester, self.locators.LOC_MORE_OPTIONS_XPATH)
        self.sleep(2)

    def click_modal_cancel_button(self, tester):
        self.click_xpath(tester, self.locators.LOC_CANCEL_BUTTON_XPATH)
        self.sleep(2)

    def click_confirm_changes_button(self, tester):
        self.click_class_and_text(tester,
            self.locators.LOC_CONFIRM_BUTTON_CLASS,
            self.labels.LBL_CHANGE_WITHDRAWAL_SCHEDULE_MODAL_CONFIRM_CHANGES
        )
        self.sleep(2)

    '''This section deals with Edit Bank Account info'''
