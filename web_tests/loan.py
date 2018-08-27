class LoanObject(object):
    #loan_type = None
    #loan_amount = None
    #loan_term = None
    #card_balance = None
    #interest_rate = None
    #apr = None
    #monthly_payment = None
    loan_types = ['Home Mortgate', 'Auto',
        'Student', 'Credit Card', 'Personal Loan',
        'Bill', 'Other']
    origination_date = {}
    #current_balance = None
    #isNewLoan = True
    #loan_dict = {}

    def __init__(self, loan_type='other', amount=0, term=0, interest=0, payment=0, newLoan=True, origin_month='January', origin_year='2000', current_balance=0):
        self.loan_dict = {}
        self.setLoanType(loan_type)
        self.setLoanAmount(amount)
        self.setLoanTerm(term)
        self.setLoanInterest(interest)
        self.setLoanPayment(payment)
        self.setNewLoan(newLoan, origin_month, origin_year, current_balance)

    def __repr__(self):
        return_string = ""
        for key in self.loan_dict.keys():
            return_string += "\n%s: %s" % (key, str(self.loan_dict[key]))
        return return_string

    def setLoanType(self, loan_type):
        if loan_type and loan_type in self.loan_types:
            self.loan_type = loan_type
            self.loan_dict['loan_type'] = loan_type
        else:
            assert(False, "Invalid Loan type argument: %s" % loan_type)

    def setLoanAmount(self, amount):
        if amount:
            if self.loan_type == 'Credit Card':
                self.credit_balance = amount
                self.loan_dict['credit_balance'] = amount
            elif self.loan_type == 'Bill':
                pass
            else:
                self.loan_amount = amount
                self.loan_dict['loan_amount'] = amount
        else:
            assert(False, "Null loan amount!")

    def setLoanTerm(self, term):
        if term:
            if self.loan_type == 'Credit Card' or self.loan_type == 'Bill':
                pass
            else:
                self.loan_term = term
                self.loan_dict['loan_term'] = term
        else:
            assert(False, "Null loan term!")

    def setLoanInterest(self, interest):
        if interest:
            if self.loan_type == 'Credit Card':
                self.apr = interest
                self.loan_dict['apr'] = interest
            elif self.loan_type == 'Bill':
                pass
            else:
                self.interest_rate = interest
                self.loan_dict['interest_rate'] = interest
        else:
            assert(False, "Null interest rate!")

    def setLoanPayment(self, payment):
        if payment:
            self.monthly_payment = payment
            self.loan_dict['monthly_payment'] = payment
        else:
            assert(False, "Null monthly payment!")

    def setNewLoan(self, newLoan, origin_month, origin_year, current_balance):
        if not newLoan:
            self.isNewLoan = False
            if self.loan_type == 'Credit Card' or self.loan_type == 'Bill':
                pass
            else:
                self.loan_dict['origination_date'] = {}
                if origin_month:
                    self.origination_date['month'] = origin_month
                    self.loan_dict['origination_date']['month'] = origin_month
                else:
                    assert False, "Null origination Month"
                if origin_year:
                    self.origination_date['year'] = origin_year
                    self.loan_dict['origination_date']['year'] = origin_year
                else:
                    assert False, "Null origination Year"
                if current_balance:
                    self.current_balance = current_balance
                    self.loan_dict['current_balance'] = current_balance
                else:
                    assert False, "Null Current Balance"
        else:
            self.isNewLoan = True
