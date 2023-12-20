import entity.Account as Account
import exception.MinBalanceException as M
class SavingsAccount(Account):
    def __init__(self,balance,customer_id,interest_rate):
        try:
            if balance<500:
                raise M.MinBalanceException
            else:
                super().__init__("Savings",balance,customer_id)
            self.interest_rate=interest_rate
        except M.MinBalanceException as M:
            print(M)