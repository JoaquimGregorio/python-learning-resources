from classes.account import Account


class SavingsAccount(Account):
    def withdraw(self, value: int | float):
        if self.balance < value:
            print("Insufficient balance.")
            return
        self.balance -= value
        self.details()
