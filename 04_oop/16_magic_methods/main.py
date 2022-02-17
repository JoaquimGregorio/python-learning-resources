"""
Magic Methods
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        # return super().__new__(cls)

        def some_func(*args, **kwargs):
            print("Some function.")

        cls.some_func = some_func  # now it`s a method

        print("__new__ initialized!")
        return object.__new__(cls)  # all classes derives from object

    def __init__(self):
        print("__init__ initialized!")


a = A()
# print(type(a))
a.some_func()


# Singleton:
class B:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        print("__init__ initialized in B!")


b1 = B()
b2 = B()
b3 = B()
print(id(b1), id(b2), id(b3))


class C:
    def __init__(self):
        pass

    # allow us to call the class instance:
    def __call__(self, *args, **kwargs):
        result = 1
        for num in args:
            result *= num
        return result


c1 = C()
print(c1(1, 2, 3, 4, 5))


class D:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        # print(key, value)
        if key == "name":
            self.__dict__[key] = "you cannot do this"
        else:
            self.__dict__[key] = value

    def __del__(self):
        print("Colleted by garbage collector")

    def __str__(self):
        return "Class D print changed."

    def __len__(self):
        return 23


d1 = D()
d1.name = "Joaquim"
d1.new_attr = "Some value"
print(d1.name)
print(d1.new_attr)
print(d1)
print(len(d1))
