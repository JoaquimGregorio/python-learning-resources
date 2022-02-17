"""
OOP - Class Method
"""


class Person:
    current_year = 2022

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_year_of_birth(self):
        print(self.current_year - self.age)

    @classmethod  # it is also a factory method
    def by_year_of_birth(cls, name: str, year_of_birth: int):
        age = cls.current_year - year_of_birth
        return cls(name, age)


# p1 = Person("Joaquim", 18)
# print(Person.current_year)
p1 = Person.by_year_of_birth("Joaquim", 2003)
print(p1.age)
p1.get_year_of_birth()
