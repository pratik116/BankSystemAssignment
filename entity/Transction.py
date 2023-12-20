from datetime import date

class Transaction:
    
    def __init__(self,account_id,transaction_type,amount):
        
        
        self.account_id=account_id
        self.date_time=date.today()
        self.transaction_type=transaction_type
        self.transaction_amount=amount