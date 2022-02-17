"""
OOP - Metaclasses
In Python everything is an object
Metaclasses are classes that create another classes
`type` is a metaclasse (!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        # Forcing class B
        if "b_speak" not in namespace:
            print(f"You need to create the `b_speak` method in {name}")
        else:
            if not callable(namespace["b_speak"]):
                print("The property `b_speak` must be a method")

        if "attr_cls" in namespace:
            del namespace["attr_cls"]  # remove overrided attribute from A subclasses

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_cls = "Value A"

    def speak(self):
        self.b_speak()


class B(A):
    attr_cls = "Value B"


b1 = B()
print(b1.attr_cls)

# Creating classe with `type` metaclass
# ex.: type(classname, superclasses, attributedict)
class Father:
    pass


C = type("C", (Father,), {"attr": "Hello world!"})
c1 = C()
print(c1.attr)
print(type(c1))
