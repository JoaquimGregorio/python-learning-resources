class Customer:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.adresses: list[Address] = []

    def add_address(self, city: str, state: str):
        self.adresses.append(Address(city, state))

    def list_adresses(self):
        for address in self.adresses:
            print(address.city, address.state)

    # This method is called when Python garbage collector removes the
    # instance of the class from memory.
    def __del__(self):
        print(f"{self.name} was deleted.")


class Address:
    def __init__(self, city: str, state: str):
        self.city = city
        self.state = state

    # This method is called when Python garbage collector removes the
    # instance of the class from memory.
    def __del__(self):
        print(f"{self.city}/{self.state} was deleted.")
