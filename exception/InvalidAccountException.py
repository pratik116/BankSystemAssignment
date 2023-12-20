class InvalidAccountException(Exception):
    def __init__(self):
        super().__init__("InvalidAccountException") 