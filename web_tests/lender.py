class LenderObject(object):
    def __init__(self, lender_name="", lender_address="", lender_account_number=0):
        self.setLenderName(lender_name)
        self.setLenderAddress(lender_address)
        self.setLenderAccountNumber(lender_account_number)

    def __repr__(self):
        return ("\nLender Name: %s\nLender Address: %s\nLender Account Number: %s" %(self.lender_name,
        self.lender_address,
        self.lender_account_number))

    def setLenderName(self, lender_name):
        if lender_name:
            self.lender_name = lender_name
        else:
            assert False, "Lender name is Null!"

    def setLenderAddress(self, lender_address):
        if lender_address:
            self.lender_address = lender_address
        else:
            assert False, "Lender address is Null!"

    def setLenderAccountNumber(self, lender_account_number):
        if lender_account_number:
            self.lender_account_number = lender_account_number
        else:
            assert False, "Lender Account Number is Null!"
