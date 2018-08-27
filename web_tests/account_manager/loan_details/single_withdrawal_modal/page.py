from QA.web_tests.core.assertions import Assertions
from QA.web_tests.account_manager.loan_details.single_withdrawal_modal.locators import SingleWithdrawalModalLocators
from QA.web_tests.account_manager.loan_details.single_withdrawal_modal.labels import SingleWithdrawalModalLabels

class SingleWithdrawalModalPage(Assertions):

    locators = SingleWithdrawalModalLocators()
    labels = SingleWithdrawalModalLabels()

    '''This section deals with the Select Single Withdrawal Date Modal'''

    def click_change_withdrawal_drop_down(self, tester):
        print("Click Change Withdrawal Drop down")
        assert_text = "Change Withdrawal Drop down element not found!"
        self.wait_for_id_displayed(tester,
            self.locators.LOC_WITHDRAWAL_DATE_TO_CHANGE_DROPDOWN_SELECT_ID,
            assert_text=assert_text
        )
        self.click_id(tester, self.locators.LOC_WITHDRAWAL_DATE_TO_CHANGE_DROPDOWN_SELECT_ID)
        self.sleep(2)

    def click_new_withdrawal_drop_down(self, tester):
        print("Click New Withdrawal Drop down")
        assert_text = "New Withdrawal Drop down element not found!"
        self.wait_for_id_displayed(tester,
            self.locators.LOC_NEW_WITHDRAWAL_DATE_DROPDOWN_SELECT_ID,
            assert_text=assert_text
        )
        self.click_id(tester, self.locators.LOC_NEW_WITHDRAWAL_DATE_DROPDOWN_SELECT_ID)
        self.sleep(2)

    def get_list_of_date_elements_from_xpath(self, tester, dropdown_list_xpath):
        self.assert_xpath(tester, dropdown_list_xpath)
        list = self.find_xpath(tester, dropdown_list_xpath)
        return list.find_elements_by_class_name(self.locators.LOC_WITHDRAWAL_DATE_LIST_ITEM_CLASS)

    def get_list_of_existing_withdrawal_dates(self, tester):
        print("Getting list of existing withdrawal dates")
        return self.get_list_of_date_elements_from_xpath(tester, self.locators.LOC_WITHDRAWAL_DATE_TO_CHANGE_LIST_XPATH)

    def get_list_of_new_withdrawal_dates(self, tester):
        print("Getting list of New withdrawal dates")
        return self.get_list_of_date_elements_from_xpath(tester, self.locators.LOC_NEW_WITHDRAWAL_DATE_LIST_XPATH)

    def get_date_text_from_panel(self, tester, panel_xpath):
        print("Getting Date text from Panel")
        self.wait_for_xpath_displayed(tester,
            panel_xpath,
            assert_text="Date Panel not displayed!"
        )
        date_text = self.find_xpath(tester, panel_xpath).text
        return date_text

    def select_date_by_text(self, tester, list_of_date_elements, text):
        for list_element in list_of_date_elements:
            if self.compare_date_entries(text, list_element.text):
                tester.execute_script("arguments[0].scrollIntoView(true);", list_element)
                list_element.click()
                self.sleep(2)
                return True
        assert False, "Date: %s could not be found in list!" % text

    def select_date_by_position(self, tester, list_of_date_elements, position=0):
        if list_of_date_elements:
            tester.execute_script("arguments[0].scrollIntoView(true);", list_of_date_elements[position])
            text = list_of_date_elements[position].get_attribute('value')
            print("Element text at position %d is %s" % (position, text))
            list_of_date_elements[position].click()
            self.sleep(2)
            return text
        else:
            assert False, "Date list is empty!"

    def select_first_date(self, tester, list_of_date_elements):
        return self.select_date_by_position(tester, list_of_date_elements)

    def select_first_existing_withdrawal_date(self, tester):
        dates = self.get_list_of_existing_withdrawal_dates(tester)
        return self.select_first_date(tester, dates)

    def select_first_new_withdrawal_date(self, tester):
        dates = self.get_list_of_new_withdrawal_dates(tester)
        return self.select_first_date(tester, dates)

    def select_all_existing_withdrawal_dates(self, tester):
        dates = self.get_list_of_new_withdrawal_dates(tester)
        for position in range(len(dates)):
            print(self.select_date_by_position(tester, dates, position))

    def select_all_new_withdrawal_dates(self, tester):
        dates = self.get_list_of_new_withdrawal_dates(tester)
        for position in range(len(dates)):
            print(self.select_date_by_position(tester, dates, position))

    def select_existing_withdrawal_date(self, tester, date_text):
        dates = self.get_list_of_existing_withdrawal_dates(tester)

        self.select_date_by_text(tester, dates, date_text)

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

    def compare_date_entries(self, first_text, second_text):
        split_one = first_text.split(' ')
        split_two = second_text.split(' ')
        print(split_one, split_two)
        if split_one[1] == split_two[1] and split_one[2] == split_two[2]:
            if split_one[0] in split_two[0] or split_two[0] in split_one[0]:
                return True
        return False
