# challenge -04
class account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
        
class savingsaccount(account):
    def __init__(self,title,balance,interestrate):
        super().__init__(title,balance)
        self.interestrate=interestrate
            
            
Account=account("ashish",5000)
SavingAccount=savingsaccount("ashish",5000,5)
print(Account.title)
print(SavingAccount.balance)