"""
while
keywords:
continue -> jump one loop cycle
break -> ends the loop
"""
x = 0
while x < 5:
    if x % 2 == 0:
        x += 1
        continue

    print(x)
    x += 1
