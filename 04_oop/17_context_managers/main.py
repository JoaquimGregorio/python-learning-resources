"""
Context Managers - creating them
"""
from contextlib import contextmanager


# The methods __enter__ and __exit__ are called only if we use the class using the `with` keywod
class File:
    def __init__(self, filename, mode):
        print("Opening file")
        self.filex = open(filename, mode)

    def __enter__(self):
        print("Returning file")
        return self.filex

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file")
        self.filex.close()
        # treat exceptions here...
        return True  # to prevent exceptions


with File("foo.txt", "w") as file1:
    file1.write("Something")

print("###############################")


# Only works with the `with` keywod too:
@contextmanager
def open_file(filename, mode):
    try:
        print("Opening file")
        filex = open(filename, mode)
        yield filex
    finally:
        print("Closing file")
        filex.close()


with open_file("foo.txt", "w") as file2:
    file2.write("Line 1\n")
    file2.write("Line 2\n")
    file2.write("Line 3\n")
