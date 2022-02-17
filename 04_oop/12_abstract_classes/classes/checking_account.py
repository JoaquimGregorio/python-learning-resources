from classes.account import Account


class CheckingAccount(Account):
    def __init__(self, agency, number, balance: int | float, limit: int | float = 10):
        super().__init__(agency, number, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, value: int | float):
        if (self.balance + self.limit) < value:
            print("Insufficient balance.")
            return
        self.balance -= value
        self.details()
