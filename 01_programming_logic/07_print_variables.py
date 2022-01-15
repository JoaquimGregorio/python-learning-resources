name = 'Joaquim'
age = 18
height = 1.76
is_of_age = age >= 18
weight = 100
imc = weight / (height ** 2)

print(name, 'is', age, 'years old and his imc is', imc)
print(f'{name} is {age} years old and his imc is {imc:.2f}')
# We can use variables anywhere using its index
print('IMC = {2:.0f}. {0} is {1} years old and his imc is {2:.2f}'.format(
    name, age, imc))
# We can give aliases to the variables
print('IMC = {im:.0f}. {n} is {a} years old and his imc is {im:.2f}'.format(
    n=name, a=age, im=imc))
