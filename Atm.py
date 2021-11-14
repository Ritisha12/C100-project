class Atm(object):
    def __init__(self,cardNo,PinNo):
        self.cardNo=cardNo
        self.PinNo=PinNo
        
    def cashWithdrawal(self):
        print("Cash Withdrawed")
    def BalanceEnquiry(self):
        print("Balance Enquiry")
    
bmw=Atm("P1S265","1637")
bmw.cashWithdrawal()
bmw.BalanceEnquiry()
