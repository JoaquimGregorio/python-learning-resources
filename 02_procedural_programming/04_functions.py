"""
More about functions
"""
# since I set a default value to an argument, after that,
# the following arguments must have a default value too
# The same pattern is valid to passing arguments when
# calling a function
def func(a, b, c="c", d=None):
    # d must have a default value
    print(f"{a}, {b}, {c}, {d}")


# here we get an error:
# func(1, b=2, c="c", 3)

# the right way:
func(1, b=2, d=3, c="c")  # any order (b, d and c)

# Without knowing the arguments:
def func2(a, b, *args, **kwargs):
    # arguments and keyword arguments
    print(a, b)
    print(args)
    print(kwargs)
    print(kwargs.get("age"))
    # different from kwargs['age'], kwargs.get('age')
    # returns a value or None if key does not exist.


func2(1, 2, 3, 4, 5, name="Joaquim", lastname="Gregório")

# Unpacking when passing the arguments:
list1 = [1, 2, 3, 4, 5]
print(*list1, sep="-")  # the same as: print(1, 2, 3, 4, 5)


## Accessing global variables:
some_var = "value"
print(some_var)


def func3():
    global some_var
    some_var = "other value"  # modifying global variable
    # now we have access to some_var global variable


func3()
print(some_var)

# here we get another error:
some_var2 = "value 2"


def func4():
    print(some_var2)
    global some_var2
    print(some_var2)
    # error: some_var2 is used prior to global declaration
