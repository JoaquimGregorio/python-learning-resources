"""
Lambda functions
"""
square = lambda x: x * x

print(square(5))

list1 = [
    ["P1", 13],
    ["P2", 7],
    ["P3", 6],
    ["P4", 45],
    ["P5", 28],
]

# list1.sort(key=lambda item: item[1], reverse=False)
# print(list1)

print(sorted(list1, key=lambda i: i[1], reverse=True))
