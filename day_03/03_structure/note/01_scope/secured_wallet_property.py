class Wallet:
    def __init__(self, initial_amount=0):
        self._amount = initial_amount

    @property
    def amount(self):
        print(f"Showing amount: {self._amount}")
        return self._amount

    @amount.setter
    def amount(self, amount):
        print(f"Setting amount to {amount}")
        self._amount += amount

food_wallet = Wallet(250)
food_wallet.amount += 1_000

print("Food Budget:", food_wallet.amount)
