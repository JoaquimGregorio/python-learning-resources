"""
Formating values with modifiers

:s - Text (string)
:d - Integers (int)
:f - Floating point numbers (float)
:.(number)f - Number of deciamal places (float)
:(character)(> or < or ^)(quantity)(type - s, d or f)

> - Left
< - Right
^ -  Center
"""
# num_1 = 10
# num_2 = 3
# quotient = num_1 / num_2
# print('{:.2f}'.format(quotient), end=' ')
# print(f'{quotient:.2f}')

# num_1 = 1
# print(f'{num_1:0>10}')  # on the left

# num_2 = 1150
# print(f'{num_2:0<10}')  # on the right

# num_3 = 1233
# print(f'{num_3:0^10}')  # on the center

# num_4 = 3455
# print(f'{num_4:0>10.2f}') # matching

# name = 'Joaquim Gregório'
# print(len(name))
# print(f'{name:#^50}')

# formated_name = '{:@>50}'.format(name)
# print(formated_name)

name = 'Joaquim Gregório'
# name = name.ljust(30, '#')
print(name.lower())
print(name.upper())
print(name.title())
