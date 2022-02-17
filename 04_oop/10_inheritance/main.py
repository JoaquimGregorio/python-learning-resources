"""
OOP - Inheritance
Association - Use a class
Aggregation - Has a class
Composition - Is owner of a class
Inheritance - Is another class
"""
from classes import Customer, Student, VIPCustomer

c1 = Customer("Joaquim", 18)
# c1.speak()
# c1.buy()
s1 = Student("Jairo", 22)
# s1.speak()
# s1.study()

c2 = VIPCustomer("Rose", "Mary", 25)
c2.speak()
