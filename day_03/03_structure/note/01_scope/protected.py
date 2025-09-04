class Wallet:
    def __init__(self, initial_amount=0):
        # Protected attribute: One underscore at the start
        # Accessible inside class and by children, discouraged outside
        self._amount = initial_amount
