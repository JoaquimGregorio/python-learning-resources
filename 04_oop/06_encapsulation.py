"""
OOP - Encapsulation
Conventional OOP: public, protected, private

In Python: (just conventions)
    _ (weak private, private or protected),
    __(private)
"""


class Database:
    def __init__(self):
        self._data = {}
        self.__name = "database"

    # Getter to get access for private attributes
    @property
    def name(self):
        return self.__name

    def add_client(self, id, name: str):
        if "clients" not in self._data:
            self._data["clients"] = {id: name}
        else:
            self._data["clients"].update({id: name})

    def list_clients(self):
        for id, name in self._data["clients"].items():
            print(id, name)

    def remove_client(self, id):
        del self._data["clients"][id]


db = Database()
db.add_client(1, "Joaquim")
db.add_client(2, "Gregório")
db.add_client(3, "Maria")

# Using __
# print(db.__name)  # Error
db.__name = "database 2"  # it will not override, just create another attribute
print(db.__name)
print(db._Database__name)  # accessing private '__name' attribute
print(db.name)  # using getter
# db.name = 'something'  # Error
