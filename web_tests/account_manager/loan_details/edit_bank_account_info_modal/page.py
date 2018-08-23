from QA.web_tests.core.assertions import Assertions
from QA.web_tests.account_manager.loan_details.edit_bank_account_info_modal.locators import EditBankAccountInfoModalLocators
from QA.web_tests.account_manager.loan_details.edit_bank_account_info_modal.labels import EditBankAccountInfoModalLabels


class EditBankAccountInfoModalPage(Assertions):

    locators = EditBankAccountInfoModalLocators()
    labels = EditBankAccountInfoModalLabels()

    def select_add_new_account_from_dropdown(self, tester):
        print("Selecting %s from drop down" % self.labels.LBL_ADD_NEW_BANK_ACCOUNT)
        assert_text = "Error locating %s drop down locator" % self.labels.LBL_ADD_NEW_BANK_ACCOUNT
        self.assert_id(tester, self.locators.LOC_BANK_SELECT_DROPDOWN_ID, assert_text=assert_text)
        self.assert_class
        return self.select_item_in_dropdown_by_text(
            tester,
            self.locators.LOC_BANK_SELECT_DROPDOWN_ID,
            self.locators.LOC_BANK_SELECT_LIST['xpath'],
            self.locators.LOC_BANK_SELECT_LIST_ITEM_CLASS,
            self.labels.LBL_ADD_NEW_BANK_ACCOUNT,
            assert_text=assert_text
        )

    def select_current_bank_from_dropdown(self, tester):
        print("Selecting %s from drop down" % self.labels.LBL_CURRENT_BANK_ACCOUNT_POSITION)
        assert_text = "Error locating %s drop down locator" % self.labels.LBL_CURRENT_BANK_ACCOUNT_POSITION
        return self.select_item_in_dropdown_by_position(
            tester,
            self.locators.LOC_BANK_SELECT_DROPDOWN_ID,
            self.locators.LOC_BANK_SELECT_LIST['xpath'],
            self.locators.LOC_BANK_SELECT_LIST_ITEM_CLASS,
            self.labels.LBL_CURRENT_BANK_ACCOUNT_POSITION,
            assert_text=assert_text
        )

    def click_connect_to_bank_button(self, tester):
        #will bring up plaid connection modal
        print("Clicking Connect to Bank button")
        try:
            return self.click_xpath(tester,
                self.locators.LOC_CONNECT_TO_BANK['xpath']
            )
        except:
            print("xpath locator strategy failed, locating by class and text")
            return self.click_class_and_text(
                tester, self.locators.LOC_CONNECT_TO_BANK['class'],
                self.labels.LBL_CONNECT_TO_YOUR_BANK,
                assert_text="Connect to Bank Button not found!"
            )

    def click_enter_bank_details_manually(self, tester):
        print("Clicking Enter Bank Details Manually button")
        #try:
        self.click_xpath(tester,
            self.locators.LOC_EDIT_BANK_DETAILS_MANUALLY['xpath'],
            assert_text='Enter Bank Details Manually button not found!'
        )

        assert_text="Text field not visible!"
        self.wait_for_id_displayed(tester, self.locators.LOC_BANK_NAME_TEXT_FIELD_ID,
            assert_text=assert_text
        )

    def click_modal_cancel_button(self, tester):
        print("Clicking modal Cancel button")
        self.click_class_and_text(
            tester,
            self.locators.LOC_BANK_EDIT_BANK_ACCOUNT_MODAL_CANCEL['class'],
            self.labels.LBL_CANCEL,
            assert_text="Modal Cancel button not found!"
        )
        self.wait_for_id_not_present(tester,
            self.locators.LOC_EDIT_BANK_ACCOUNT_MODAL_FORM_ID
        )

    def enter_new_bank_name(self, tester, bank_name_text):
        print("Entering New Bank Name: %s" % bank_name_text)
        assert_text="Bank Name text field not found!"
        self.assert_id(tester,
            self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_BANK_NAME_ID,
            assert_text=assert_text
        )
        self.type_text(
            self.find_id(tester,
                self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_BANK_NAME_ID),
            bank_name_text
        )

    def enter_new_bank_routing_number(self, tester, bank_routing_number):
        print("Entering New Bank Routing Number: %s" % bank_routing_number)
        assert_text="Bank Routing Number text field not found!"
        self.assert_id(tester,
            self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ROUTING_NUMBER_ID,
            assert_text=assert_text
        )
        self.type_text(
            self.find_id(tester,
                self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ROUTING_NUMBER_ID),
            bank_routing_number
        )

    def enter_new_bank_account_number(self, tester, bank_account_number):
        print("Entering New Bank Account Number: %s" % bank_account_number)
        assert_text="Bank Routing Number text field not found!"
        self.assert_id(tester,
            self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_NUMBER_ID,
            assert_text=assert_text
        )
        self.type_text(
            self.find_id(tester,
                self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_NUMBER_ID),
            bank_account_number
        )

    def select_account_type_by_text(self, tester, text):
        print("Selecting Account Type By Text: %s" % text)
        return self.select_item_in_dropdown_by_text(
            tester,
            self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_ID,
            self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_LIST['xpath'],
            self.locators.LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_LIST_ITEM_CLASS,
            text
        )

    def enter_new_bank_info(self, tester, new_bank_info_dict):
        print("Entering New Bank Info")
        self.enter_new_bank_name(tester, new_bank_info_dict['bank_name'])
        self.select_account_type_by_text(tester, new_bank_info_dict['account_type'])
        self.enter_new_bank_routing_number(tester, new_bank_info_dict['routing_number'])
        self.enter_new_bank_account_number(tester, new_bank_info_dict['account_number'])
        self.click_edit_new_bank_info_confirm_button(tester)

    def click_edit_new_bank_info_confirm_button(self, tester):
        print("Clicking Confirm Button")
        self.wait_for_class_and_text(
            tester,
            self.locators.LOC_EDIT_BANK_ACCOUNT_CONFIRM_BUTTON['class'],
            self.labels.LBL_CONFIRM,
            assert_text="Confirm Button not found!"
        )
        self.click_class_and_text(
            tester,
            self.locators.LOC_EDIT_BANK_ACCOUNT_CONFIRM_BUTTON['class'],
            self.labels.LBL_CONFIRM,
            assert_text="Confirm Button not found!"
        )
        #self.wait_for_id_not_present(tester,
        #    self.locators.LOC_EDIT_BANK_ACCOUNT_MODAL_FORM_ID
        #)

    def get_bank_name(self, tester):
        print("Getting Bank Name")
        self.wait_for_id(tester,
            self.locators.LOC_BANK_NAME_TEXT_FIELD_ID
        )
        return self.get_field_value_by_id(tester, self.locators.LOC_BANK_NAME_TEXT_FIELD_ID)

    def get_account_type(self, tester):
        print("Getting Account Type")
        self.wait_for_id(tester,
            self.locators.LOC_ACCOUNT_TYPE_TEXT_FIELD_ID,
        )
        return self.get_field_value_by_id(tester, self.locators.LOC_ACCOUNT_TYPE_TEXT_FIELD_ID)

    def get_bank_routing_number(self, tester):
        print("Getting Bank Routing Number")
        self.wait_for_id(tester,
            self.locators.LOC_ROUTING_NUMBER_TEXT_FIELD_ID,
        )
        return self.get_field_value_by_id(tester, self.locators.LOC_ROUTING_NUMBER_TEXT_FIELD_ID)

    def get_account_number(self, tester):
        print("Getting Account Number")
        self.wait_for_id(tester,
            self.locators.LOC_ACCOUNT_NUMBER_TEXT_FIELD_ID,
        )
        return self.get_field_value_by_id(tester, self.locators.LOC_ACCOUNT_NUMBER_TEXT_FIELD_ID)

    def get_bank_info(self, tester):
        print("Getting Bank Info")
        bank_info = {}
        bank_info['bank_name'] = self.get_bank_name(tester)
        bank_info['account_type'] = self.get_account_type(tester)
        bank_info['routing_number'] = self.get_bank_routing_number(tester)
        bank_info['account_number'] = self.get_account_number(tester)
        account_info_string="Bank Name: %s\
        \nAccount Type: %s\
        \nRouting Number: %s\
        \nAccount Number: %s" % (bank_info['bank_name'],
            bank_info['account_type'],
            bank_info['routing_number'],
            bank_info['account_number']
        )
        return bank_info
