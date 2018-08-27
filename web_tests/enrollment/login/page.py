from QA.web_tests.account_manager.login.page import AccountManagerLoginPage
from QA.web_tests.enrollment.login.locators import LoginPageLocators
from QA.web_tests.enrollment.login.labels import LoginLabels

class EnrollmentLoginPage(AccountManagerLoginPage):

    def __init__():
        self.locators = LoginPageLocators()

    def check_successful_login(self, tester):
        print("Verifying login was successful")
        assert_text = "Login failed. Login "
        self.wait_for_xpath_not_present(tester, self.locators.LOC_SUBMIT_BUTTON_XPATH)
