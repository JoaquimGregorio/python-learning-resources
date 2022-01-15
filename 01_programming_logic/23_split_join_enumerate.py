"""
Split, Join, Enumerate
* split - split a string # str
* join - join a list # str
* enumerate - enumerate elements of a list # iterables
"""
string = "O Brasil é o país do futebol, o Brasil é penta."
list1 = string.split(" ")
list2 = string.split(",")

word = ""
counter = 0
for value in list1:
    occurrences = list1.count(value)

    if occurrences > counter:
        counter = occurrences
        word = value

print(f"The word that appeared most times is {word} ({counter}x)")

for value in list2:
    print(value.strip().capitalize())

## Join ##
string2 = "O Brasil é penta."
list3 = string2.split(" ")
string3 = ",".join(list3)
print(string3)

## Enumerate ##
for i, value in enumerate(list3, 10):
    print(i, value)

# This is exactly what enumerate() does, but it does it in a tuple
list4 = [[0, "Joaquim"], [1, "Marcos"], [2, "Carlos"]]

for i, value in list4:
    print(i, value)

# Unpacking
l1, l2, l3 = list4
print(l1)
