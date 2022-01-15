"""
for / else
else is called when the loop ends without breaking (break)
"""
list1 = ["sJoaquim", "André", "Carlos"]

for el in list1:
    print(el)
    if el.lower().startswith("j"):
        break
else:
    print("There's no word that starts with J.")
