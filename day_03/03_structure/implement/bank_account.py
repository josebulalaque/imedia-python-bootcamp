class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError()

        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError()

        self.balance -= amount

    def print_balance(self):
        print(self.balance)
