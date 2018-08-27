from QA.web_tests.core.assertions import Assertions
from QA.web_tests.account_manager.main_page.locators import AccountManagerMainPageLocators
from QA.web_tests.account_manager.main_page.labels import AccountManagerMainlabels


class AccountManagerMainPage(Assertions):
    locators = AccountManagerMainPageLocators()
    labels = AccountManagerMainlabels()

    def select_edit_my_info_button(self, tester):
        print("Clicking Edit My Info button")
        self.click_class_and_text(tester, self.locators.LOC_EDIT_MY_INFO_BUTTON_CLASS,
            self.labels.LBL_EDIT_MY_INFORMATION)

    def get_email_text(self, tester):
        print("Getting email text")
        return self.get_field_value_by_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_EMAIL_ID)

    def get_primary_phone_text(self, tester):
        print("Getting primary phone #")
        return self.get_field_value_by_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_PRIMARY_PHONE_ID)

    def get_secondary_phone_text(self, tester):
        print("Getting secondary phone #")
        return self.get_field_value_by_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_SECONDARY_PHONE_ID)

    def get_address_text(self, tester):
        print("Getting home address")
        return self.get_field_value_by_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_ADDRESS_ID)

    def set_email_text(self, tester, email_text):
        print("Setting email text: %s" % email_text)
        self.assert_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_EMAIL_ID,
            assert_text="Email field couldn't be found")
        element = self.find_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_EMAIL_ID)
        element.clear()
        self.type_text(element, email_text)
        if self.get_email_text(tester) != email_text:
            assert False, "Email was not changed!"

    def set_primary_phone_text(self, tester, phone_text):
        print("Setting primary phone #: %s" % phone_text)
        self.assert_id(tester,
            self.locators.LOC_EDIT_MY_INFO_MODAL_PRIMARY_PHONE_ID,
            assert_text="Primary phone field couldn't be found"
        )
        element = self.find_id(tester,
            self.locators.LOC_EDIT_MY_INFO_MODAL_PRIMARY_PHONE_ID
        )
        element.clear()
        self.type_text(element, phone_text)
        if self.get_primary_phone_text(tester) != phone_text:
            assert False, "Primary phone number was not changed!"

    def set_secondary_phone_text(self, tester, phone_text):
        print("Setting secondary phone #: %s" % phone_text)
        self.assert_id(tester,
            self.locators.LOC_EDIT_MY_INFO_MODAL_SECONDARY_PHONE_ID,
            assert_text="Secondary phone field couldn't be found"
        )
        element = self.find_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_SECONDARY_PHONE_ID)
        element.clear()
        self.type_text(element, phone_text)
        if self.get_secondary_phone_text(tester) != phone_text:
            assert False, "Secondary phone number was not changed!"

    def set_address_text(self, tester, address_text):
        print("Setting address text: %s" % address_text)
        self.assert_id(tester,
            self.locators.LOC_EDIT_MY_INFO_MODAL_ADDRESS_ID,
            assert_text="Address field couldn't be found"
        )
        element = self.find_id(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_ADDRESS_ID)
        element.clear()
        self.type_text(element, address_text)
        if self.get_address_text(tester) != address_text:
            assert False, "Address was not changed!"

    def click_confirm_button(self, tester):
        print("Clicking confirm button")
        modal_object = self.find_class(tester, self.locators.LOC_EDIT_MY_INFO_MODAL_BODY_CLASS)
        assert_text = "Confirm button not found!"
        self.wait_for_xpath(tester, self.locators.LOC_EDIT_MY_INFO_CONFIRM_BUTTON_XPATH,
            assert_text=assert_text
        )
        #confirm_button = modal_object.find_element_by_xpath(self.locators.LOC_EDIT_MY_INFO_CONFIRM_BUTTON_XPATH)
        self.click_xpath(tester, self.locators.LOC_EDIT_MY_INFO_CONFIRM_BUTTON_XPATH,
            assert_text=assert_text
        )
        assert_text = "Edit My Information Modal not closed!"
        self.wait_for_class_not_present(tester,
            self.locators.LOC_EDIT_MY_INFO_MODAL_BODY_CLASS,
            assert_text=assert_text
        )

    def click_loan_panel(self, tester, position=0):
        print("Clicking loan panel at position %d" % position)
        self.wait_for_css_displayed(tester, self.locators.LOC_LIST_LOAN_OBJECT_CSS)
        loan_panels = tester.find_elements_by_css_selector(self.locators.LOC_LIST_LOAN_OBJECT_CSS)
        if not loan_panels:
            return None
        else:
            loan_panels[position].click()
