"""
OOP - Composition
One class owns another that is removed when the owner is removed
"""
from classes import Customer

c1 = Customer("Joaquim", 18)
c1.add_address("Ibiapina", "CE")
print(c1.name)
c1.list_adresses()
del c1  # __del__ method is called
print()

c2 = Customer("Maria", 55)
c2.add_address("Salvador", "BA")
c2.add_address("Rio de Janeiro", "RJ")
print(c2.name)
c2.list_adresses()
print()

c3 = Customer("João", 19)
c3.add_address("São Paulo", "SP")
print(c3.name)
c3.list_adresses()
print()

# To see when the garbage collector removes the instances from the memory
print("################################")
