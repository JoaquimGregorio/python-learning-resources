"""
Reduce
"""
from data import products, people, list_1
from functools import reduce

## Bad way:
accumulator = 0
for i in list_1:
    accumulator += i
# print(accumulator)

# Good, but simple, way:
# print(sum(list_1))

# Reduce way:
list_sum = reduce(lambda ac, i: i + ac, list_1, 0)
print(list_sum)

## Prices sum:
prices_sum = reduce(lambda ac, p: p["price"] + ac, products, 0)
print(prices_sum)
