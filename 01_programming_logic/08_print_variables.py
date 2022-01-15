name = 'Joaquim'
age = 18
height = 1.76
weight = 100
current_year = 2021
year_of_birth = current_year-age
imc = weight/(height**2)

print(f'{name} is {age} years old, {height} tall and weights {weight}kg.')
print(f'{name}\'s IMC is {imc:.2f}')
print(f'{name} was born in {year_of_birth}')
