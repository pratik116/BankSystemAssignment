import entity.Account as A

class CurrentAccount(A.Account):
    def __init__(self,balance,customer,overdraft_limit=1000):
        super().__init__("Current",balance,customer)
        self.overdraft_limit=overdraft_limit