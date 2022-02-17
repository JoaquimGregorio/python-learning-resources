from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, number, balance: int | float):
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

    @balance.setter
    def balance(self, value: int | float):
        # if not isinstance(value, (int, float)):
        #     raise ValueError('Account balance must be a number.')
        self._balance = value

    def deposit(self, value: int | float):
        self.balance += value
        self.details()

    def details(self):
        print(f"Account agency: {self.agency}", end=" ")
        print(f"Account number: {self.number}", end=" ")
        print(f"Account balance: {self.balance}")

    @abstractmethod
    def withdraw(value):
        pass
