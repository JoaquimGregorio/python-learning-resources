"""
Sets
add, update, clear, discard
union |
intersection &
difference -
symetric_difference ^
"""
s1 = {1, 2, 3, 4, 5}

# A set is not subscriptable, then we cannot access a value directly

for v in s1:
    print(v)


s2 = set()
s2.add(1)
s2.add("a")
s2.add((2,))
s2.add(3)
print(s2)
s2.discard("a")
print(s2)
s2.update("bcde")  # unpack an iterable element
print(s2)
# In sets, elements are not in order like in lists
# Using lists:
l1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 7, 8, 9, "Joaquim", "Joaquim"]
print(l1)
l1 = list(set(l1))
print(l1)

s3 = {1, 2, 3, "a", "b", "c"}
s3.clear()
print(s3)
