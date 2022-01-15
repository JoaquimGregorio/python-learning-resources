"""
Count - Itertools
"""
from types import GeneratorType
from itertools import count

var = zip("Hello", "Hello")
var = ((x, y) for x, y in var)
print(isinstance(var, GeneratorType))
for val in var:
    print(val)

counter = count(start=5, step=0.3)  # we can pass floats and negative values

for value in counter:
    print(round(value, 2))

    if value >= 10:
        break
