class ChangeWithdrawalScheduleModalLocators():
    '''change withdrawal schedule modal'''
    
    LOC_CLEAR_SELECTIONS_CLASS = 'subtext'

    #Every Other week

    LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_ID = "pay-freq-schedule-forms-select" #Drop down for Schedule
    LOC_PAY_FREQ_SCHEDULE_FORMS_SELECT_XPATH = '//*[@id="pay-freq-schedule-forms-select"]'
    LOC_PAY_FREQ_SCHEDULE_LIST_XPATH = '//*[@id="pay-freq-schedule-forms"]/div[2]/div'
    LOC_PAY_FREQ_SCHEDULE_LIST_ITEM_CLASS = "eu-btn"

    #Common to weekly and bi-weekly options.
    LOC_PAY_WEEKDAY_SCHEDULE_FORMS_SELECT_ID = "pay-weekday-schedule-forms-select" #Drop down for weekday
    LOC_PAY_WEEKDAY_SCHEDULE_LIST_XPATH = '//*[@id="pay-weekday-schedule-forms"]/div[2]/div'
    LOC_PAY_WEEKDAY_SCHEDULE_LIST_ITEM_CLASS = "eu-btn"

    LOC_PAY_BIWEEKLY_SCHEDULE_FORMS_SELECT_ID = "pay-biweekly-schedule-forms-select"
    LOC_PAY_BIWEEKLY_SCHEDULE_LIST_XPATH = '//*[@id="pay-biweekly-schedule-forms"]/div[2]/div'
    LOC_PAY_BIWEEKLY_SCHEDULE_LIST_ITEM_CLASS = "eu-btn"

    #Semi Monthly

    LOC_PAY_SEMI_MONTHLY_SCHEDULE_FORMS_SELECT_ID = "pay-semi-month-schedule-forms-select"
    LOC_PAY_SEMI_MONTHLY_SCHEDULE_LIST_XPATH = '//*[@id="pay-semi-month-schedule-forms"]/div[2]/div'
    LOC_PAY_SEMI_MONTHLY_SCHEDULE_ITEM_CLASS = "eu-btn"

    #Monthly

    LOC_PAY_MONTHLY_SCHEDULE_FORMS_SELECT_ID = "pay-monthly-schedule-forms-select"
    LOC_PAY_MONTHLY_SCHEDULE_LIST_XPATH = '//*[@id="pay-monthly-schedule-forms"]/div[2]/div'
    LOC_PAY_MONTHLY_SCHEDULE_LIST_ITEM_CLASS = "eu-btn"

    LOC_CHANGE_SINGLE_WITHDRAWAL_DATE_LINK_XPATH = '//*[@id="step1"]/div[1]/p/a'

    LOC_NEXT_BUTTON_XPATH = '//*[@id="set-schedule"]/div[1]/div[4]/div/button[1]'
    LOC_MORE_OPTIONS_XPATH = '//*[@id="set-schedule"]/div[1]/div[4]/div/button[2]'
    LOC_CANCEL_BUTTON_XPATH = '//*[@id="change-withdrawal-form"]/div[1]/div[8]/div/button'
    LOC_CONFIRM_BUTTON_CLASS = "eu-btn"
    LOC_WITHDRAWAL_PAY_SCHEDULE_LIST_ITEM_CLASS = "eu-btn"

    LOC_CHANGE_WITHDRAWAL_SCHEDULE_MODAL_CLASS = "modal-body"
    LOC_CHANGE_WITHDRAWAL_PAY_SCHEDULE_DROPDOWN_ID = "pay-freq-schedule-forms-select"
