"""
isnumeric, isdigit, isdecimal -> bool
They don't work with float.
"""
num1 = input("Type a number: ")
num2 = input("Type another number: ")

if num1.isdecimal() and num2.isdecimal():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print("Cannot convert input into numbers.")
