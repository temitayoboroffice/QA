from QA.web_tests.core.assertions import Assertions
from QA.web_tests.account_manager.loan_details.change_withdrawal_schedule_modal.locators import ChangeWithdrawalScheduleModalLocators
from QA.web_tests.account_manager.loan_details.change_withdrawal_schedule_modal.labels import ChangeWithdrawalScheduleModalLabels

class ChangeWithdrawalScheduleModalPage(Assertions):

    locators = ChangeWithdrawalScheduleModalLocators()
    labels = ChangeWithdrawalScheduleModalLabels()

    def click_clear_selections_link(self, tester):
        print("Clicking Clear Selections link")
        self.assert_class_and_text(tester,
            self.locators.LOC_CLEAR_SELECTIONS_CLASS,
            self.labels.LBL_CLEAR_SELECTIONS,
            assert_text="%s link not found!" % self.labels.LBL_CLEAR_SELECTIONS
        )
        self.click_class_and_text(tester,
            self.locators.LOC_CLEAR_SELECTIONS_CLASS,
            self.labels.LBL_CLEAR_SELECTIONS
        )

    def click_pay_freq_schedule_dropdown(self, tester, text_option):
        print("Clicking Schedule dropdown")
        assert_text = "Schedule drop down not found!"
        self.wait_for_id(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_ID,
            assert_text=assert_text
        )
        self.click_id(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_ID,
            assert_text=assert_text
        )
        self.sleep(2)
        #self.click_xpath(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_XPATH,
        #    assert_text=assert_text
        #)

    def click_pay_day_dropdown(self, tester):
        print("Clicking Pay day dropdown")
        assert_text = "Pay day drop down not found!"
        self.click_id(tester, self.locators.LOC_PAY_WEEKDAY_SCHEDULE_FORMS_SELECT_ID,
            assert_text=assert_text
        )
        self.sleep(2)

    def get_list_of_freq_schedule_elements(self, tester):
        print("Getting list of schedule elements")
        assert_text = "Schedule list element not found!"
        self.wait_for_xpath(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_LIST_XPATH,
            assert_text=assert_text
        )
        list = self.find_xpath(tester, self.locators.LOC_PAY_FREQ_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_WITHDRAWAL_PAY_SCHEDULE_LIST_ITEM_CLASS)

    def get_pay_day_list(self, tester):
        print("Getting list of Pay day elements")
        assert_text = "Pay day list element not found!"
        self.assert_xpath(tester, self.locators.LOC_PAY_WEEKDAY_SCHEDULE_LIST_XPATH,
            assert_text=assert_text
        )
        list = self.find_xpath(tester, self.locators.LOC_PAY_WEEKDAY_SCHEDULE_LIST_XPATH)
        return list.find_elements_by_class_name(self.locators.LOC_PAY_WEEKDAY_SCHEDULE_LIST_ITEM_CLASS)

    def select_pay_schedule_by_text(self, tester, list_of_schedule_elements, text):
        print("Selecting pay schedule: %s" % text)
        assert list_of_schedule_elements, "Found empty list of schedule elements!"
        return self.select_element_from_list_by_text(tester, list_of_schedule_elements, text)

    def select_pay_day_by_text(self, tester, list_of_days, text):
        print("Selecting pay day: %s" % text)
        assert list_of_days, "Found empty list of schedule pay day elements!"
        return self.select_element_from_list_by_text(tester, list_of_days, text)

    def click_biweekly_schedule_dropdown(self, tester):
        print("Clicking Bi-Weekly schedule dropdown")
        assert_text = "Bi-Weekly schedule drop down not found!"
        self.click_id(tester, self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_FORMS_SELECT_ID,
            assert_text=assert_text
        )
        self.sleep(2)

    def get_biweekly_pay_dates_list(self, tester):
        print("Getting list of Bi-weekly pay dates")
        assert_text = "Bi-Weekly date list element not found!"
        list = self.find_xpath(tester, self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_LIST_XPATH)
        assert list, assert_text
        return list.find_elements_by_class_name(self.locators.LOC_PAY_BIWEEKLY_SCHEDULE_LIST_ITEM_CLASS)

    def select_biweekly_pay_date(self, tester, list_of_dates, text):
        print("Selecting Bi-Weekly pay date: %s" % text)
        assert list_of_dates, "Found empty list of pay date elements!"
        return self.select_element_from_list_by_text(tester, list_of_dates, text)

    def click_bimonthly_schedule_dropdown(self, tester):
        print("Clicking Bi-Monthly schedule dropdown")
        assert_text = "Bi-Monthly schedule drop down not found!"
        self.click_id(tester, self.locators.LOC_PAY_SEMI_MONTHLY_SCHEDULE_FORMS_SELECT_ID,
            assert_text=assert_text
        )
        self.sleep(2)

    def get_bimonthly_pay_dates_list(self, tester):
        print("Getting list of Bi-Monthly pay dates")
        assert_text = "Bi-Monthly date list element not found!"
        list = self.find_xpath(tester, self.locators.LOC_PAY_SEMI_MONTHLY_SCHEDULE_LIST_XPATH)
        assert list, assert_text
        return list.find_elements_by_class_name(self.locators.LOC_PAY_SEMI_MONTHLY_SCHEDULE_ITEM_CLASS)

    def select_bimonthly_pay_date(self, tester, list_of_bimonthly_dates, text):
        print("Selecting Bi-Monthly pay date: %s" % text)
        assert list_of_dates, "Found empty list of pay date elements!"
        return self.select_element_from_list_by_text(tester, list_of_bimonthly_dates, text)

    def click_monthly_schedule_dropdown(self, tester):
        print("Clicking Monthly schedule dropdown")
        assert_text = "Monthly schedule drop down not found!"
        self.click_id(tester, self.locators.LOC_PAY_MONTHLY_SCHEDULE_FORMS_SELECT_ID,
            assert_text=assert_text
        )
        self.sleep(2)

    def get_month_dates_list(self, tester):
        print("Getting list of Monthly pay dates")
        assert_text = "Monthly date list element not found!"
        list = self.find_xpath(tester, self.locators.LOC_PAY_MONTHLY_SCHEDULE_LIST_XPATH)
        assert list, assert_text
        return list.find_elements_by_class_name(self.locators.LOC_PAY_MONTHLY_SCHEDULE_LIST_ITEM_CLASS)

    def select_date_of_the_month(self, tester, list_of_monthly_dates, text):
        print("Selecting date of the Month: %s" % text)
        assert list_of_dates, "Found empty list of Month date elements!"
        return self.select_element_from_list_by_text(tester, list_of_monthly_dates, text)

    def select_pay_schedule(self, tester, schedule_dict):
        print("Selecting Pay Schedule: %s" % schedule_dict['schedule_type'])
        type = schedule_dict['schedule_type']
        self.click_clear_selections_link(tester)
        self.click_pay_freq_schedule_dropdown(tester, type)
        schedule_list = self.get_list_of_freq_schedule_elements(tester)
        self.select_pay_schedule_by_text(tester, schedule_list, schedule_dict['schedule_type'])
        if type == self.labels.LBL_WEEKLY_SCHEDULE:
            pay_day = schedule_dict['pay_day']
            self.click_pay_day_dropdown(tester)
            pay_day_list = self.get_pay_day_list(tester)
            self.select_pay_day_by_text(tester, pay_day_list, pay_day)
        elif type == self.labels.LBL_EVERY_OTHER_WEEK_SCHEDULE:
            pay_day = schedule_dict['pay_day']
            self.click_pay_day_dropdown(tester)
            pay_day_list = self.get_pay_day_list(tester)
            self.select_pay_day_by_text(tester, pay_day_list, pay_day)
            pay_date = schedule_dict['next_pay_day']
            self.click_biweekly_schedule_dropdown(tester)
            pay_date_list = self.get_biweekly_pay_dates_list(tester)
            self.select_biweekly_pay_date(tester, pay_date_list, pay_date)
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
        print("Clicking Next button in modal")
        assert_text = "Modal Next button not found!"
        self.click_xpath(tester, self.locators.LOC_NEXT_BUTTON_XPATH,
            assert_text=assert_text
        )

    def click_modal_more_options_button(self, tester):
        print("Clicking More Options button in modal")
        assert_text = "Modal More Options button not found!"
        self.click_xpath(tester, self.locators.LOC_MORE_OPTIONS_XPATH,
            assert_text=assert_text
        )

    def click_modal_cancel_button(self, tester):
        print("Clicking Cancel button in modal")
        assert_text = "Modal Cancel button not found!"
        self.click_xpath(tester, self.locators.LOC_CANCEL_BUTTON_XPATH,
            assert_text=assert_text
        )
        assert_text = "Change Withdrawal Schedule Modal not closed!"
        self.wait_for_class_not_present(tester,
            self.locators.LOC_CHANGE_WITHDRAWAL_SCHEDULE_MODAL_CLASS,
            assert_text=assert_text
        )

    def click_confirm_changes_button(self, tester):
        print("Clicking Confirm Changes button in modal")
        assert_text = "Modal Confirm Changes Options button not found!"
        self.click_class_and_text(tester,
            self.locators.LOC_CONFIRM_BUTTON_CLASS,
            self.labels.LBL_CHANGE_WITHDRAWAL_SCHEDULE_MODAL_CONFIRM_CHANGES,
            assert_text=assert_text
        )
        assert_text = "Change Withdrawal Schedule Modal not closed!"
        self.wait_for_class_not_present(tester,
            self.locators.LOC_CHANGE_WITHDRAWAL_SCHEDULE_MODAL_CLASS,
            assert_text=assert_text
        )
