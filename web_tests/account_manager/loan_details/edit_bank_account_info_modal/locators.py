class EditBankAccountInfoModalLocators():

    '''Edit Bank Account Modal'''
    LOC_EDIT_BANK_ACCOUNT_MODAL_FORM_ID = 'edit-bank-account-form'
    LOC_BANK_SELECT_DROPDOWN_ID = 'bank-select-select'
    LOC_BANK_SELECT_LIST = {
        'class':'select-list',
        'attribute':'for',
        'for':LOC_BANK_SELECT_DROPDOWN_ID,
        'xpath':'//*[@id="bank-select"]/div[2]/div'
    }
    LOC_BANK_SELECT_LIST_ITEM_CLASS = "eu-btn"
    LOC_ADD_NEW_BANK_ACCOUNT_LINK = '//*[@id="edit-bank-account-form"]/div[1]/div[1]/a'
    LOC_BANK_NAME_TEXT_FIELD_ID = 'bank-name'
    LOC_ACCOUNT_TYPE_TEXT_FIELD_ID = 'bank-type-input'
    LOC_ROUTING_NUMBER_TEXT_FIELD_ID = 'bank-routing'
    LOC_ACCOUNT_NUMBER_TEXT_FIELD_ID = 'bank-accountNo'
    LOC_BANK_EDIT_BANK_ACCOUNT_MODAL_CONFIRM = {
        'css':'button',
        'type':'submit',
        'attribute':'xpath',
        'class':'eu-btn',
        'xpath':'//*[@id="edit-bank-account-form"]/div[1]/div[5]/div/button[1]'
    }
    LOC_BANK_EDIT_BANK_ACCOUNT_MODAL_CANCEL = {
        'css':'button',
        'attribute':'xpath',
        'class':'eu-btn-secondary',
        'xpath':'//*[@id="edit-bank-account-form"]/div[1]/div[5]/div/button[2]'
    }

    '''Only when "Add a New Account" is selected'''

    LOC_CONNECT_TO_BANK = {
        'css':'button',
        'attribute':'xpath',
        'class':'eu-btn',
        'xpath':'//*[@id="add-account-btns"]/button[1]'
    }

    LOC_EDIT_BANK_DETAILS_MANUALLY = {
        'css':'button',
        'attribute':'xpath',
        'class':'eu-btn',
        'xpath':'//*[@id="add-account-btns"]/button[2]'
    }

    LOC_BANK_ADD_NEW_BANK_ACCOUNT_CANCEL = {
        'css':'button',
        'attribute':'xpath',
        'class':'eu-btn-secondary',
        'xpath':'//*[@id="edit-bank-account-form"]/div[1]/div[5]/div/button'
    }

    LOC_PLAID_LINK_CONTAINER_ID = 'plaid-link-container'

    LOC_PLAID_CONTINUE_BUTTON = {
        'css':'button',
        'attribute':'xpath',
        'class':'Button--is-plaid-color',
        'xpath':'//*[@id="plaid-link-container"]/div/div[1]/div/div/div[2]/div[2]/button'
    }

    LOC_PLAID_INSTITUTION_SELECT_PANE_BUTTON = {
        'class':'InstitutionSelectPaneButton',
        'attribute':'data-institution'
    }

    LOC_PLAID_USERNAME_ID = 'username'
    LOC_PLAID_PASSWORD_ID = 'password'

    LOC_PLAID_LOGIN_SUBMIT = {
        'class':'Button',
        'type':'submit',
        'xpath':'//*[@id="plaid-link-container"]/div/div[1]/div/div[2]/div[3]/form/button'
    }

    LOC_PLAID_NAVBAR_IS_CONNECTED_PANE = {
        'class':'Navbar--is-ConnectedPane',
        'xpath':'//*[@id="plaid-link-container"]/div/div[1]/div/div[2]/div[1]'
    }

    LOC_PLAID_CONNECTED_PRIMARY_HEADING = {
        'class':'primary-heading primary-heading--has-margin-bottom',
        'tag':'h1',
        'xpath':'//*[@id="plaid-link-container"]/div/div[1]/div/div[2]/div[3]/div[1]/h1'
    }

    LOC_PLAID_CONNECTED_CONTINUE = {
        'class':'Button',
        'type':'button',
        'xpath':'//*[@id="plaid-link-container"]/div/div[1]/div/div[2]/div[3]/div[2]/button'
    }

    LOC_PLAID_CHECKING_RADIO_ID = 'account-0'
    LOC_PLAID_SAVINGS_RADIO_ID = 'account-1'

    LOC_EDIT_BANK_ACCOUNT_CONFIRM_BUTTON = {
        'type':'submit',
        'class':'eu-btn',
        'xpath':'//*[@id="edit-bank-account-form"]/div[1]/div[5]/div/button[1]'
    }

    LOC_EDIT_BANK_ACCOUNT_CANCEL_BUTTON = {
        'type':'button',
        'class':'eu-btn-secondary',
        'xpath':'//*[@id="edit-bank-account-form"]/div[1]/div[5]/div/button[2]'
    }

    LOC_ADD_BANK_ACCOUNT_MANUALLY_BANK_NAME_ID = 'bank-name'
    LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_ID = 'bank-type-select'
    LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_LIST = {
        'class':'select-list',
        'attribute':'for',
        'for':LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_ID,
        'xpath':'//*[@id="bank-type"]/div[2]/div'
    }

    LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_DROPDOWN_LIST_ITEM_CLASS = 'eu-btn'
    LOC_ADD_BANK_ACCOUNT_MANUALLY_ROUTING_NUMBER_ID = 'bank-routing'
    LOC_ADD_BANK_ACCOUNT_MANUALLY_ACCOUNT_NUMBER_ID = 'bank-accountNo'
