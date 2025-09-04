class Wallet:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def __add__(self, other):
        new_amount = self.amount + other.amount
        return Wallet(new_amount)


food_wallet = Wallet(250)
transport_wallet = Wallet(1000)
total_wallet = food_wallet + transport_wallet

print("Food Budget: ", food_wallet.amount)
print("Transport Budget: ", transport_wallet.amount)
print("Total Budget: ", total_wallet.amount)
