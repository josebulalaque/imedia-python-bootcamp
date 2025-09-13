class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError()
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError()
        self.__balance -= amount

    def print_balance(self):
        print(self.__balance)


bank1 = BankAccount()
bank1.deposit(1000)
bank1.print_balance()
bank1.withdraw(500)
bank1.print_balance()
