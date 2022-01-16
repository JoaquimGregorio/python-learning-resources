"""
Decorators
"""


def master(func):
    def slave(*args, **kwargs):  # if args are needed
        print("Now I'm decorated.")
        func(*args, **kwargs)

    return slave


@master
def say_hello():
    print("Hello")


say_hello()

# It does something like this:
# say_hello = master(say_hello)


@master
def another_func(msg: str):
    print(msg)


another_func("Hello Zevietana")
