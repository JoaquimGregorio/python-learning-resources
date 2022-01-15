"""
Data input
"""
name = input("What is your name? ")
age = input("What is your age? (years) ")
year_of_birth = 2021 - int(age)

print(f"{name} is {age} years old. " f"{name} was born in {year_of_birth}")
