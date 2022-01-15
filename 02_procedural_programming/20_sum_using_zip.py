"""
TODO
"""
from itertools import zip_longest

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

lists_sum = [x + y for x, y in zip(list_a, list_b)]
print(lists_sum)

lists_sum = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(lists_sum)
