"""
List Comprehension
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('List 1:', l1)

ex1 = [el for el in l1]
print(ex1)

ex2 = [el for el in l1 if el % 2 == 0]
print(ex2)

ex3 = [el * 2 for el in l1]
print(ex3)

ex4 = [(x, y) for x in l1 for y in range(3)]
print(ex4)

l2 = ['Luiz', 'Mauro', 'Maria']

ex5 = [v.replace('a', '@').upper() for v in l2]
print(ex5)

t1 = (
    ('key 1', 'value 1'),
    ('key 2', 'value 2'),
)

ex6 = [(y, x) for x, y in t1]
ex6 = tuple(ex6)
print(ex6)

l3 = list(range(100))
ex7 = [el for el in l3 if el % 3 == 0 if el % 8 == 0]
print(ex7)

ex8 = [el if el % 3 == 0 and el % 8 == 0 else "it's not" for el in l3]
print(ex8)
