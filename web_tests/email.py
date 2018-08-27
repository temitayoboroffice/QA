import datetime

class EarnUpEmail(object):

    default_domain = 'mailinator.com'
    default_user_pref = 'test_user'


    def __init__(self, user=None, domain=None):
        self.user = ''
        self.domain = ''
        if not user:
            self.user = self.new_user()
        if not domain:
            self.domain = self.default_domain
        self.text = self.user+'@'+self.domain


    def new_user(self, user_prefix=None):
        current_datetime = datetime.datetime.now()
        time_formatted_text = current_datetime.strftime("%Y%m%d%H%M%S")
        if not user_prefix:
            user_prefix = self.default_user_pref
        local = user_prefix + time_formatted_text
        return local
