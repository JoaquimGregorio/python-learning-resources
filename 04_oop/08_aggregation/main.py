"""
OOP - Aggregation
"""
from classes import ShoppingCart, Product

shopping_cart = ShoppingCart()

p1 = Product("Shirt", 50)
p2 = Product("IPhone", 10000)
p3 = Product("Cup", 15)

shopping_cart.add_product(p1)
shopping_cart.add_product(p2)
shopping_cart.add_product(p3)
shopping_cart.add_product(p3)
shopping_cart.add_product(p2)
shopping_cart.add_product(p1)
shopping_cart.add_product(p1)

shopping_cart.list_products()
print(shopping_cart.total_sum)
