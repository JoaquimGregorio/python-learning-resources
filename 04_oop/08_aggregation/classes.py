class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.name, product.value)

    @property
    def total_sum(self):
        total = sum([product.value for product in self.products])
        return total


class Product:
    def __init__(self, name: str, value):
        self.name: str = name
        self.value: float = value
