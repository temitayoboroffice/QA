from QA.web_tests.core.assertions import Assertions
from QA.web_tests.account_manager.login.locators import AccountManagerLoginLocators

class AccountManagerLoginPage(Assertions):

    locators = AccountManagerLoginLocators()

    def login(self, tester, username, password):
        print("\nLogging into Account manager")
        self.wait_for_id(tester, self.locators.LOC_USERNAME_ID)
        print("Entering username: %s" %username)
        self.type_text(self.find_id(tester, self.locators.LOC_USERNAME_ID), username)
        self.assert_id(tester, self.locators.LOC_PASSWORD_ID)
        print("Entering password: %s" %password)
        self.type_text(self.find_id(tester, self.locators.LOC_PASSWORD_ID), password)
        self.click_xpath(tester, self.locators.LOC_LOGIN_BUTTON_XPATH)
