"""
Sets
"""
s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
print(s1)
print(s2)
print("union:")
print(s1 | s2)  # we can use s1.union() function
print("intersection:")
print(s1 & s2)
print("difference:")
print(s1 - s2)
print("simetric_difference:")
print(s1 ^ s2)

l1 = ["Luiz", "João", "Maria"]
l2 = ["João", "Maria", "Maria", "Luiz", "Luiz", "Luiz", "Luiz"]

print(l1 == l2)

l1 = set(l1)
l2 = set(l2)

print(l1 == l2)

l1 = list(l1)  # by coincidence, l1 and l2 can be in the same order
l2 = list(l2)

print(l1 == l2)
