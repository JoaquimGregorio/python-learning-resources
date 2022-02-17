"""
OOP - Static Methods
"""
from random import randint


class Person:
    current_year = 2022

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_year_of_birth(self):
        print(self.current_year - self.age)

    @classmethod
    def by_year_of_birth(cls, name: str, year_of_birth: int):
        age = cls.current_year - year_of_birth
        return cls(name, age)

    @staticmethod  # without access to csl or self
    def generate_id():
        rand = randint(10000, 99999)
        return rand


p1 = Person.by_year_of_birth("Joaquim", 2003)
print(p1.age)
p1.get_year_of_birth()
print(Person.generate_id())
print(p1.generate_id())
