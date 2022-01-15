"""
Functions (2)
"""


def quotient(n1: int, n2: int):
    if n2 == 0:
        return

    return n1 / n2


result = quotient(2, 0)

if result:
    print("{:.2f}".format(result))
else:
    print("Invalid.")


def f(msg):
    print(msg)


def dumb():
    return f


var = dumb()


print(id(f), id(var))


if var == f:
    print("var is equals to f")
else:
    print("pass")
