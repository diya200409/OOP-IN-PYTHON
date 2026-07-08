class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
            print("New Balance:", self.balance)
        else:
            print("Insufficient Balance.")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating Object
atm1 = ATM(5000, 1234)

# Checking Balance
atm1.check_balance()

# Deposit
atm1.deposit(1000)

# Withdraw
atm1.withdraw(2000)

# Checking Balance Again
atm1.check_balance()