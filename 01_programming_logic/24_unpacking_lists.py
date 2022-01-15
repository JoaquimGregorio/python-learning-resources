"""
Unpacking lists
"""
list1 = ["João", "Luis", "Maria", 1, 2, 3, 4, 5]

n1, n2, *other_list, last_value = list1  # you can use *_

print(n1, n2)
print(other_list)
print(last_value)

## Inverting variable values
x = 1
y = "a"
print(f"x: {x}, y: {y}")

[x, y] = [y, x]
print(f"x: {x}, y: {y}")

x, y = y, x
print(f"x: {x}, y: {y}")
