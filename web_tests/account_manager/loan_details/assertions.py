from QA.web_tests.account_manager.loan_details.page import AccountManagerLoanDetailsPage

class AccountManagerLoanDetailsAssertions(AccountManagerLoanDetailsPage):

    def assert_correct_schedule_in_panel(self, tester, schedule_text):
        detail_view_panel_schedule = self.get_current_schedule_from_detail_view(tester)
        assert(detail_view_panel_schedule == schedule_text,
            "Schedule indicated in loan details panel does not match expected Schedule:\
             \nExpected Schedule: %s\nObserved Schedule: %s\n" % (schedule_text,
                detail_view_panel_schedule
            )
        )
        print('Expected Schedule Found: %s' % schedule_text)
