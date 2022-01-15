"""
Dictionary Comprehension
"""
list1 = [
    ("key1", "value1"),
    ("key2", "value2"),
]

d1 = {x.title(): y.upper() for x, y in list1}
print(d1)

d2 = {f"key_{x}": f"value_{x}" for x in range(4)}
print(d2)
