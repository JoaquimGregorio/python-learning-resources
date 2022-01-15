"""
if, elif e else
You can use relational operators:
== > >= < <= !=
You can use relational keywords:
and, or, not, in, not in
You can use the 'pass' keyword to avoid empty 'if' statement
"""
if 2 >= 3 and 1 == 1:
    print("True.")
elif not False:
    print("Now it's true.")
elif 1 > 2 or 3 < 4:
    pass
else:
    print("It's not true.")

# Short hand if .. else
a = 2
b = 330
print("A") if a > b else print("=") if a == b else print("B")

name = "Joaquim Gregório"
if "uim" in name:
    print("There's 'uim' in your name.")
if "w" not in name:
    print("There's no 'w' character in your name.")
