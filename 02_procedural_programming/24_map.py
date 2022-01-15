"""
Map
"""
from data import products, people, list_1

# new_list = map(lambda item: item * 2, list_1)
# new_list = list(new_list)
# new_list = [x * 2 for x in list_1]
# print(new_list)


### Using dictionaries:
def increase_price(product: dict):
    product["price"] = round(product["price"] * 1.05, 2)
    return product


new_products = map(increase_price, products)
for product in new_products:
    print(product)


names = map(lambda p: p["name"], people)
for person in names:
    print(person)
