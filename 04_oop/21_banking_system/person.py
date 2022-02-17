class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) >= 3:
            self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int):
        self._age = new_age
