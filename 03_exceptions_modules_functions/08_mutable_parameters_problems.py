"""
Mutable: Lists, Dictionaries
Immutable: Tuples, Strings, Numbers, Booleans, None
"""
from typing import Iterable

# The problem is that mutable default values as parameters can point to the same
# place in the momory and then we can work with the same object without knowing it.
# def clients_list(clients_iterable: Iterable[str], listx: list = []):
def clients_list(clients_iterable: Iterable[str], listx: list = None):
    if listx is None:
        listx = []
    listx.extend(clients_iterable)
    return listx


# Or we can just create pass the second argument as an empty list
clients1 = clients_list(["John", "Mary", "Stewart"], [])
clients2 = clients_list(["Marcos", "Steve", "Bob"])
clients3 = clients_list(["Joseph"])

print(clients1)
print(clients2)
