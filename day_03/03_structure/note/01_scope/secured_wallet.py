class Wallet:
    def __init__(self, initial_amount=0):
        self._amount = initial_amount

    def get_amount(self):
        print(f"Showing amount: {self._amount}")
        return self._amount

    def set_amount(self, amount):
        print(f"Setting amount to {amount}")
        self._amount += amount

food_wallet = Wallet(250)
food_wallet.set_amount(food_wallet.get_amount() + 1_000)

print("Food Budget:", food_wallet.get_amount())
