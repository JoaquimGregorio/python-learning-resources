"""
Combinations, Permutations, Product -> Itertools
Combination - Order doesn`t matter
Permutation - Order does matter
Both don`t repeat unique values

Product - Order does matter and repeats unique values
"""
from itertools import combinations, permutations, product

people = ["Joaquim", "André", "Márcia", "Maria", "Lúcia", "Joana"]

# for group in combinations(people, 2):
#     print(group)

# for group in permutations(people, 2):
#     print(group)

for group in product(people, repeat=2):
    print(group)
