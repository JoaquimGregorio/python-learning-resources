from person import Person
from account import SavingsAccount, CheckingAccount


class Client(Person):
    def __init__(self, name: str, age: int, account: SavingsAccount | CheckingAccount):
        super().__init__(name, age)
        self._account = account

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, _):
        pass  # cannot set client account directly
