class Account:
    def __init__(self, initial_balance=0):
        # Private attribute: Two underscores at the start
        # Accessible inside class only
        self.__balance = initial_balance