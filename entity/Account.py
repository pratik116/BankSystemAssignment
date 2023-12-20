class Account:
    prevAccountNumber=1000

    def __init__(self,Customers_id,type,balance):
        self._Customer_id=Customers_id
        self._accNo=Account.prevAccountNumber+1
        Account.prevAccountNumber=self._accNo
        self._type=type
        self._balance=balance

    @property
    def get_accNo(self):
        return self._accNo
    @property
    def get_type(self):
        return self._type
    @property
    def get_balance(self):
        return self._balance
    @property
    def get_Customer_id(self):
        return self._Customer_id
    
    def set_accNo(self,accNo):
        self._accNo=accNo

    def set_type(self,type):
        self._type=type

    def set_balance(self,balance):
        self._balance=balance


    def printAccountInfo(self):
        print("Account Number:",self._accNo)
        print("Account Type:",self._type)
        print("Account Balance:",self._balance)