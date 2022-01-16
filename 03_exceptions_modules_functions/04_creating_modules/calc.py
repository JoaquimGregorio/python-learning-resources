import math

PI = math.pi


def duplicate_list(listx: list) -> list:
    return [x * 2 for x in listx]


def multiply_list(listx: list[int] | list[float]):
    r = 1
    for i in listx:
        r *= i
    return r


# The following code avoid the code inside the if confition being
# executed by other file that is importing the current module, since
# the variable __name__ is "__main__" only when we execute the file
# directly, otherwise, the __name__ variable will be the module name
# that is the file name. So, we can avoid the code inside if confition
# being executed when we import this module in other file.
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    print(duplicate_list(list1))
    print(multiply_list(list1))
    print(PI)

    # __name__ only returns the module's name if that
    # module is being imported in other file
    print(__name__)
