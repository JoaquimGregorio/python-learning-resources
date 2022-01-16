"""
Deleting files
"""
import os

with open("demofile2.txt", "w+") as file:
    file.write("Some line 1\n")
    file.write("Some line 2\n")
    file.write("Some line 3\n")

# Delete:
os.remove("demofile2.txt")
