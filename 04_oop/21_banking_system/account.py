from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, number: int, balance: int):
        self._agency = agency
        self._number = number
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    def deposit(self, value: int):
        if value > 0:
            self._balance += value

    @abstractmethod
    def withdraw(self, value: int):
        pass


class SavingsAccount(Account):
    def __init__(self, agency: int, number: int, balance: int):
        super().__init__(agency, number, balance)

    def withdraw(self, value: int):
        if value <= self._balance:
            self._balance -= value


class CheckingAccount(Account):
    def __init__(self, agency: int, number: int, balance: int, limit: int):
        super().__init__(agency, number, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value: int):
        if value > self._limit:
            self._limit = value

    def withdraw(self, value: int):
        if value <= (self._balance + self._limit):
            self._balance -= value
