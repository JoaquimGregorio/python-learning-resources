"""
Custom Class Exceptions
"""
# by convention the name ends with `Error`
class ItsWrongError(Exception):
    pass


def func():
    raise ItsWrongError("It's wrong from my custom error class.")


try:
    func()
except ItsWrongError as error:
    print(f"Error: {error}")
