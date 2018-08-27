from QA.web_tests.pay_schedule import PaySchedule

class ChangeWithdrawalScheduleModalLabels():

    LBL_EVERY_OTHER_WEEK_SCHEDULE_TEXT = "every other week withdrawal schedule"
    LBL_WEEKLY_SCHEDULE_TEXT = "weekly withdrawal schedule"
    LBL_TWICE_A_MONTH_SCHEDULE_TEXT = "twice a month withdrawal schedule"
    LBL_ONCE_A_MONTH_SCHEDULE_TEXT = "once a month withdrawal schedule"
    LBL_CHANGE_WITHDRAWAL_SCHEDULE_MODAL_CONFIRM_CHANGES = "Confirm Changes"
    LBL_CLEAR_SELECTIONS = "Clear Selections"

    def __init__(self):
        every_other_week = self.LBL_EVERY_OTHER_WEEK_SCHEDULE_TEXT.upper()
        weekly = self.LBL_WEEKLY_SCHEDULE_TEXT.upper()
        twice_a_month = self.LBL_TWICE_A_MONTH_SCHEDULE_TEXT.upper()
        once_a_month = self.LBL_ONCE_A_MONTH_SCHEDULE_TEXT.upper()
        schedule_options = [schedule.upper() for schedule in PaySchedule.schedule_types]
        self.LBL_WEEKLY_SCHEDULE = PaySchedule.schedule_types[0]
        self.LBL_EVERY_OTHER_WEEK_SCHEDULE = PaySchedule.schedule_types[1]
        self.LBL_TWICE_A_MONTH_SCHEDULE = PaySchedule.schedule_types[2]
        self.LBL_MONTHLY_SCHEDULE = PaySchedule.schedule_types[3]

        self.schedule_dict = {}

        for index in range(len(schedule_options)):
            if schedule_options[index] in every_other_week:
                self.schedule_dict[self.LBL_EVERY_OTHER_WEEK_SCHEDULE_TEXT] = PaySchedule.schedule_types[index]
            if schedule_options[index] in weekly:
                self.schedule_dict[self.LBL_WEEKLY_SCHEDULE_TEXT] = PaySchedule.schedule_types[index]
            if schedule_options[index] in twice_a_month:
                self.schedule_dict[self.LBL_TWICE_A_MONTH_SCHEDULE_TEXT] = PaySchedule.schedule_types[index]
            if schedule_options[index] in once_a_month:
                self.schedule_dict[self.LBL_ONCE_A_MONTH_SCHEDULE_TEXT] = PaySchedule.schedule_types[index]
