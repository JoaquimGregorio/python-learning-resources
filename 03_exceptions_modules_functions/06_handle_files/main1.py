"""
Context managers - better that use try...except...finally to handle files
"""
# It closes the file automatically
with open("demofile1.txt", "w+") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

    file.seek(0, 0)
    print(file.read())

# Read mode:
with open("demofile.txt", "r") as file:
    print(file.read())

# Append mode:
# 'a+' mode will append whatever you write without clear the file content
