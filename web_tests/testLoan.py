from loan import LoanObject
from lender import LenderObject
from pay_schedule import PaySchedule

myLoan = LoanObject(loan_type='Personal Loan', amount=20000, term=3,
    interest=2.1, payment=200)
print(myLoan)

myLoan2 = LoanObject(loan_type='Credit Card', amount=200000, term=3,
    interest=2.2, payment=400)
print(myLoan2)

myLoan3 = LoanObject(loan_type='Bill', amount=20000, term=3,
    interest=2.1, payment=200)
print(myLoan3)

myLoan4 = LoanObject(loan_type='Personal Loan', amount=200000, term=3,
    interest=2.1, newLoan=False, payment=200, current_balance=180000)
print(myLoan4)

myLender1 = LenderObject(lender_name='ACME Loans', lender_address='555 Cliffside Ave',
    lender_account_number = 1221633950333)
print(myLender1)

mySchedule = PaySchedule(next_pay_day="August 17th")
print (mySchedule)

mySchedule2 = PaySchedule(type="Every Other Week", day_of_week="Friday", next_pay_day="August 10th")
print (mySchedule2)

mySchedule3 = PaySchedule(type="Twice a Month", next_pay_day="August 10th")
print (mySchedule3)
