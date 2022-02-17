"""
The dataclass module provides a decorator and functions to create
methods automatically, like __init__(), __repr__(), __eq__(), etc
This creates a normal class
PEP 557 >
Python 3.7 >
https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass, field, asdict, astuple

# eq: add support to '==' operator
# repr: print the class
# init: add __init__() method automatically
# order: add suport to sort classes
# frozen: immutable class

# We can use __post_init__() to verify anything we want

# @dataclass
@dataclass(eq=False, repr=True, order=False, frozen=False, init=True)
class Person:
    name: str
    lastname: str = field(default="Some name", repr=False)
    # removing 'lastname' field from class repr

    def __post_init__(self):
        self.full_name = f"{self.name} {self.lastname}"

p1 = Person(name="Joaquim", lastname="Gregorio")
print(p1)
print(p1.full_name)
print(asdict(p1))
print(astuple(p1))
