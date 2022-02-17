from client import Client
from account import Account, SavingsAccount, CheckingAccount


class Bank:
    def __init__(self, agency: int):
        self._agency = agency
        self.__clients: list[Client] = []
        self.__accounts: list[SavingsAccount | CheckingAccount] = []

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, _):
        pass  # cannot set the bank agency

    def get_client(self, name: str, agency: int, number: int):
        for client in self.__clients:
            if (
                name == client.name
                and agency == self._agency
                and number == client.account.number
            ):
                return client
        return None
