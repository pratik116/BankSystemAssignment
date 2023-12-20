class InsufficientFundException(Exception):
    def __init__(self):
        super().__init__("InsufficientFundException")