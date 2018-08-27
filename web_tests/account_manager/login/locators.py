class AccountManagerLoginLocators():
    LOC_HEADER_IMAGE_LINK = '//*[@id="app"]/div/nav/div[1]/a/img'
    LOC_USERNAME_ID = "email"
    LOC_PASSWORD_ID = "password"
    LOC_LOGIN_BUTTON_XPATH = '//*[@id="login"]/div[3]/div[3]/div/button[1]'
    LOC_GET_YOUR_PASSWORD_XPATH = '//*[@id="login"]/div[3]/div[3]/div/button[2]'
    LOC_EMAIL_TOOLTIP_XPATH = '//*[@id="login"]/div[3]/div[2]/div[1]'
    LOC_EMAIL_TOOLTIP_SUBTEXT_XPATH = "%s/div" % LOC_EMAIL_TOOLTIP_XPATH
    LOC_PASSWORD_TOOLTIP_XPATH = '//*[@id="login"]/div[3]/div[2]/div[2]'
    LOC_PASSWORD_TOOLTIP_SUBTEXT_XPATH = "%s/div" % LOC_PASSWORD_TOOLTIP_XPATH
    LOC_SET_PASSWORD_LINK = '//*[@id="login"]/div[3]/div[2]/div[1]/div/a[1]'
    LOC_CUSTOMER_SUPPORT_PHONE_NUMBER_LINK = '//*[@id="login"]/div[3]/div[2]/div[1]/div/a[2]'
    LOC_LOADING_INDICATOR_CLASS = 'loadingIndicator'
