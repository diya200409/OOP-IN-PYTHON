class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def check_balance(self):
        print("Balance:", self.balance)

user = ATM(5000)
user.deposit(1000)
user.check_balance()