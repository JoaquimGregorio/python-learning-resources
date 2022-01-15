"""
Dictionaries
"""
import copy

customers = {
    "customer1": {"name": "Joaquim", "lastname": "Gregório"},
    "customer2": {"name": "Marcos", "lastname": "Silva"},
}

for customer_k, customer_v in customers.items():
    print(f"Showing {customer_k}")
    for data_k, data_v in customer_v.items():
        print(f"\t{data_k}: {data_v}")

d1 = {1: "a", 2: "b", 3: "c"}
v = d1  # it's not a copy
v[1] = "othe value"
print(d1)
print(v)

d2 = {1: "a", 2: "b", 3: "c", 4: ["d", "e", "f"]}
v2 = d2.copy()  # now it's a shallow copy
# Only tuples will not change
# Check why it's a shallow copy:
v2[4][0] = "D"  # notice that it will change in d2 too
print(d2[4], id(d2))
print(v2[4], id(v2))

# How to make a real copy:
d3 = {1: "a", 2: "b", 3: "c", 4: ["d", "e", "f"]}
v3 = copy.deepcopy(d3)  # independent copy

# Check why it's a shallow copy:
v3[4][0] = "D"  # notice that it will not change in d2 too
print(d3[4])
print(v3[4])


# Casting:
list1 = [
    ["c1", 1],
    ["c2", 2],
    ["c3", 3],
]
list2 = [
    ("c1", 1),
    ("c2", 2),
    ("c3", 3),
]
list3 = (
    ["c1", 1],
    ["c2", 2],
    ["c3", 3],
)
list4 = (
    ("c1", 1),
    ("c2", 2),
    ("c3", 3),
)

d4 = dict(list1)
d5 = dict(list2)
d6 = dict(list3)
d7 = dict(list4)
print(d4)
print(d5)
print(d6)
print(d7)


# Some methods:
d8 = {"a": 2, 3: 4, "b": 6, 7: 8}
d8.pop("b")
d8.popitem()  # remove the last item
print(d8)

d9 = {"str": "value", 9: 10}
d8.update(d9)
print(d8)
