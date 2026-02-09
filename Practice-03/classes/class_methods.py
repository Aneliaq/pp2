# Instance methods

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)

