"""
https://docs.python.org/3/library/functions.html#open
File handling
'r' -> open for reading (default)
'w' -> open for writing, truncating the file first
'x' -> open for exclusive creation, failing if the file already exists
'a' -> open for writing, appending to the end of the file if it exists
'b' -> binary mode
't' -> text mode (default)
'+' -> open a disk file for updating (reading and writing)
"""
file = open("demofile.txt", "w+")
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

# Since we are in the end of the file, we must seek for a relative position,
# then we can read the file.
file.seek(0, 0)
print("Reading lines...")
print(file.read())
print("###################")

file.seek(0, 0)
print(file.readline(), end="")  # now the cursor is at the end of the line read
print(file.readline(), end="")
print(file.readline(), end="")
print("###################")

file.seek(0, 0)
# print(file.readlines())  # list with the lines
for line in file.readlines():
    print(line, end="")
# Also works:
# for line in file:
#     print(line, end="")


file.close()  # it`s mandatory to prevent problems
