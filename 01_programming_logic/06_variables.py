"""
Variables:
Start with letter, can contain numbers, separate with _, lowercase letters
"""
name = 'Joaquim'
age = 18
height = 1.76
is_of_age = age >= 18
weight = 100

imc = weight / (height ** 2)

# print('Name:', name)
# print('Age:', age)
# print('Height:', height)
# print('Is of age?', is_of_age)

print(name, 'is', age, 'years old and his imc is', imc)
