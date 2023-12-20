class MinBalanceException(Exception):
    def __init__(self):
        super().__init__("Minimum balance for a savings account is 500.")