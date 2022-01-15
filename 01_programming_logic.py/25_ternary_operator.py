"""
Ternary operator
"""
# logged_user = False
# if logged_user:
#     msg = "User is logged in."
# else:
#     msg = "User needs to login."

logged_user = False

msg = "User is logged in." if logged_user else "User needs to login."

print(msg)

age = input("Type your age: ")

if not age.isnumeric():
    print("Type only numbers.")
else:
    age = int(age)
    is_of_legal_age = age >= 18

    msg2 = "Can access." if is_of_legal_age else "Cannot access."

    print(msg2)

# Expressions with OR operator
name = input("Type your name: ")

# if name:
#     print(name)
# else:
#     print("You didn't type anything.")

# msg = name or "You didn't type anything."
# print(msg)

print(name or "You didn't type anything.")
