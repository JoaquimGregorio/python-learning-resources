"""
Python lists

slicing

append(element)
insert(index, element)
pop(index?)
del / del(element, range of elements, or entire list)
clear
extend

min(list)
max(list)

range

list -> class that converts an iterable to a list
"""
# list1 = list(("a", "b", "c", "d", "e", "f", 1, 2, False))
# for el in list1:
#     print(el)
# print(list1)

l1 = list(range(1, 7))

l1.append(7)
l1.insert(0, 8)
del l1[1]  # also works like a function
del l1[3:5]

print(l1)
print(max(l1))
print(min(l1))

l2 = ["a", "ab", "abc", "abcd", "abcde"]
print(max(l2))
print(min(l2))

l3 = ["String", True, 10, -20.5]
for elem in l3:
    print(f"The type of elem is {type(elem)} and its type is {elem}")

# Using List Comprehension
[print(el) for el in l3]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

# General syntax: newlist = [expression for item in iterable if condition == True]
# expression can be whatever you want

# Creating a list with the user input (Hangman Game)
secret = "hello"
typed = []
chances = 3

while True:
    if chances == 0:
        print("You lose!")
        break

    letter = input("Type a letter: ")

    if len(letter) > 1:
        print("Type only one letter!")
        chances -= 1
        continue

    typed.append(letter)

    if letter in secret:
        print(f'Nice, the letter "{letter}" is in the secret word.')
    else:
        print(f'Hurr, the letter "{letter}" isn\'t in the secret word.')
        typed.pop()
        chances -= 1

    secret_buffer = ""
    for secret_letter in secret:
        if secret_letter in typed:
            secret_buffer += secret_letter
        else:
            secret_buffer += "*"

    if secret_buffer == secret:
        print(f'\nNice, you won!!!\nThe secret word is "{secret_buffer}"')
        break
    else:
        print(secret_buffer)

    print(f"You still have {chances} chances.")
