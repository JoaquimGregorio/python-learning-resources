"""
Zip - Joining Iterables
Zip_longest - Itertools
"""
from itertools import zip_longest, count

cities = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo"]
states = ["SP", "MG", "BA"]
index = count()
states_and_cities = zip(index, states, cities)
for value in states_and_cities:
    print(value)

# print(dict(states_and_cities))
# print(list(states_and_cities))

index = count()
## We can ommit fillvalue
states_and_cities_long = zip_longest(index, states, cities, fillvalue="None value")
# print(list(states_and_cities_long))
# for value in states_and_cities_long:
#     print(value) # infinity loop
