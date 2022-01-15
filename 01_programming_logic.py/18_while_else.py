"""
while / else
"""
x = 1
y = 1

while x <= 100:
    if x == 7:
        break  # since here the while condition is already true
    print(x, y)
    x += y
    y += 1
else:  # is execute if the while condition is false
    print("Else after while")

print("After while / else")  # is executed when the while statement ends
