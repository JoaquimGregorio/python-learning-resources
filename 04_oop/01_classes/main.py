"""
Object Oriented Programming - Classes
"""
from person import Person

p1 = Person("Joaquim", 18)
p1.eat("Pastel")
p1.stop_eating()
p1.stop_eating()
p1.eat("BOLO")
p1.stop_eating()
p1.speak("OOP")

# class variable
print(p1.current_year)
print(Person.current_year)

print(p1.get_year_of_birth())
