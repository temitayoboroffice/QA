from datetime import date, timedelta

class PaySchedule(object):
    schedule_types = ['Weekly', 'Every Other Week', 'Twice a Month', 'Once a Month']

    pay_days = ['Monday', 'Friday']
    bimonthly_pay_dates = [(1,15), (5,20), (10,25)]

    def __init__(self, type='Weekly', day_of_week='Monday', next_pay_day='January 1st',
        bimonthly_pay_date=(1,15), monthly_pay_date='15th', payment_due_date='31st'):
        self.payment_due_dates = [self.transform_integer_to_nth(digit) for digit in range(1,32)]
        self.schedule_dict = {}
        self.set_pay_schedule(type)
        if 'Week' in self.get_pay_schedule():
            self.set_day_of_eow_pay(day_of_week)
            if self.get_pay_schedule() == 'Every Other Week':
                self.set_next_pay_day(next_pay_day)
        elif self.get_pay_schedule() == 'Twice a Month':
            if bimonthly_pay_date not in self.bimonthly_pay_dates:
                assert False, "Invalid pay dates! %s" % (self.transform_date_tuples_to_nth(bimonthly_pay_date))
            self.set_bimonthly_pay_date(bimonthly_pay_date)
        elif self.get_pay_schedule() == 'Once a Month':
            self.set_monthly_pay_date(monthly_pay_date)
        else:
            assert False, "Invalid schedule option selected!"
        self.set_payment_due_date(payment_due_date)

    def __repr__(self):
         return_string = ""
         for key in self.schedule_dict.keys():
             return_string += "\n%s: %s" % (key, str(self.schedule_dict[key]))
         return return_string

    def set_pay_schedule(self, sched_type):
        if sched_type not in self.schedule_types:
            assert False, "Schedule Type is invalid!"
        self.pay_schedule = sched_type
        self.schedule_dict['schedule_type'] = sched_type

    def get_pay_schedule(self):
        return self.pay_schedule

    def set_day_of_eow_pay(self, day):
        if day not in self.pay_days:
            assert False, "Invalid pay day: %s" %day
        else:
            self.eow_pay_day = day
            self.schedule_dict['pay_day'] = day

    def get_day_of_eow_pay(self):
        return self.eow_pay_day

    def set_next_pay_day(self, payday):
        if payday not in self.return_next_two_eow_options():
            payday = self.next_pay_day = self.return_next_two_eow_options()[0]
        else:
            self.next_pay_day = payday
        self.schedule_dict['next_pay_day'] = payday

    def get_next_pay_day(self):
        return self.next_pay_day

    def set_bimonthly_pay_date(self, bimonthly_tuple):
        self.bimonthly_pay_date = bimonthly_tuple
        self.schedule_dict['bimonthly_pay_date'] = self.transform_date_tuples_to_nth(bimonthly_tuple)

    def get_bimonthly_pay_date(self):
        return self.bimonthly_pay_date

    def set_monthly_pay_date(self, paydate):
        if paydate not in self.payment_due_dates:
            assert False, "Invalid Pay date: %r" % paydate
        self.monthly_pay_date = paydate
        self.schedule_dict['monthly_pay_date'] = paydate

    def get_monthly_pay_date(self):
        return self.monthly_pay_date

    def set_payment_due_date(self, payment_due_date):
        if payment_due_date not in self.payment_due_dates:
            assert False, "Invalid Payment due date: %r" % payment_due_date
        self.payment_due_date = payment_due_date
        self.schedule_dict['payment_due_date'] = payment_due_date

    def return_future_payday_options(self, week_count):
        future_payday_options=[]
        if not self.eow_pay_day:
            assert False, "Need none null every other weekly payday"
        today = date.today()
        for offset in range(1,(week_count*7)+1):
            weekday = today + timedelta(days=offset)#date(today.year, today.month, today.day+offset)
            if weekday.strftime("%A") == self.eow_pay_day:
                future_payday_options.append("%s %s"%(weekday.strftime("%B"),
                self.transform_integer_to_nth(today.day+offset)))
        return future_payday_options

    def return_next_two_eow_options(self):
        return self.return_future_payday_options(2)

    def transform_date_tuples_to_nth(self, date_tuple):
        return("%s and %s" % (self.transform_integer_to_nth(date_tuple[0]),
            self.transform_integer_to_nth(date_tuple[1])))

    def transform_integer_to_nth(self, date_integer):
        if str(date_integer)[-1] == '1':
            if date_integer == 11:
                return str(date_integer)+'th'
            else:
                return str(date_integer)+'st'
        elif str(date_integer)[-1] == '2':
            if date_integer == 12:
                return str(date_integer)+'th'
            else:
                return str(date_integer)+'nd'
        elif str(date_integer)[-1] == '3':
            if date_integer == 13:
                return str(date_integer)+'th'
            else:
                return str(date_integer)+'rd'
        else:
            return str(date_integer)+'th'
