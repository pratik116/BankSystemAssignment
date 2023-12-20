import entity.Account as A

class ZeroBalanceAccount(A.Account):
    def __init__(self,customer_id):
        super().__init__("ZeroBalance",0,customer_id)