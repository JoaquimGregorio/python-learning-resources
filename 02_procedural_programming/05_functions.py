"""
TODO
"""
## 1
def func1(func):
    return func()


def func2():
    return "Hello world!"


print(func1(func2))

## 2
def main(func, *args, **kwargs):
    return func(*args, **kwargs)


def greeting(msg="Hello", name="user"):
    return f"{msg} {name}"


def say_hi(msg="Hi"):
    return msg


print(main(greeting, "Hi", "greeting function"))
print(main(say_hi, "Hi 2"))
