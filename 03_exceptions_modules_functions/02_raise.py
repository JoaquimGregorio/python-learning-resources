"""
Raise -> errors
https://docs.python.org/3/library/exceptions.html
"""


# You can use `raise` alone to raise the same error
# or with an error class
def quotient(n1: int | float, n2: int | float):
    if int(n2) == 0:
        raise ValueError("You cannot divide by zero.")
    return n1 / n2


try:
    print(quotient(12.1, 0))
except ValueError as err:
    print(err)


def convert_to_num(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
            pass


while True:
    number = convert_to_num(input("Type some number: "))

    if number == None:  # functions return None by default
        print("Error: it's not a number.")
    else:
        print(number * 2)
