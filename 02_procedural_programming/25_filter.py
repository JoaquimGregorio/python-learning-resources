"""
Filter
"""
from data import products, people, list_1

new_products = filter(lambda p: p["price"] >= 10, products)
for product in new_products:
    print(product)

new_people = filter(lambda p: p["age"] < 18, people)
for person in new_people:
    print(person)
