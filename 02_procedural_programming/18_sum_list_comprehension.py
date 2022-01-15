"""
TODO
"""
cart = []
cart.append(("Product 1", 30))
cart.append(("Product 2", 20))
cart.append(("Product 3", 50))
cart.append(("Product 4", 36.10))

total = sum([float(value) for _name, value in cart])
print(total)
