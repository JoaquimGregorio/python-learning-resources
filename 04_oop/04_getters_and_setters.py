"""
OOP - Getters and Setters
"""


class Product:
    def __init__(self, name: str, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.title()

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ""))
        self._price = value


p1 = Product("Shirt", 50)
p1.discount(10)
print(p1.price)

p2 = Product("PANTIES", "R$12")
print(p2.name)
print(p2.price)
