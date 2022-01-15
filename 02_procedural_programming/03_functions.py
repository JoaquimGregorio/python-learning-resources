"""
TODO
"""

## 1
def greeting(msg="Hello", name="user"):
    print(f"{msg} {name}")


greeting("Hi", "João")


## 2
def sum(n1=0, n2=0, n3=0):
    print(n1 + n2 + n3)


sum(1, 2, 3)


## 3
def increase_percentage(val=0, percentage=0):
    return val + (val * (percentage / 100))


print(increase_percentage(120, 12))

## 4
def fizz_buzz(num: int):
    by_5 = num % 5 == 0
    by_3 = num % 3 == 0
    if by_5 and by_3:
        return "FizzBuzz"
    if by_5:
        return "Buzz"
    if by_3:
        return "Fizz"

    return num


print(fizz_buzz(15))
