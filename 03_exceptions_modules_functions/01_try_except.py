"""
Try, Except
"""
try:
    # a = []
    a = {}
    print(a[1])
except NameError as err:
    # this will take the specified error
    print("Some error occurred.")
except (IndexError, KeyError) as err:
    # this will take the specified error
    print("Some index or key error.")
except Exception as err:
    # this will take any error
    print("Unexpected error.")
else:
    # Executed when there's no error
    print("The code has no error.")
finally:
    # Since this code block will always be executed,
    # you can handle the possible errors here.
    print("Finally is always executed.")
