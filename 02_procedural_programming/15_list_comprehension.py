"""
TODO
"""
string = "012345678901234567890123456789012345678901234567890123456789"
n = 10
list1 = [string[i : i + n] for i in range(0, len(string), n)]
print(list1)
new_string = ".".join(list1)
print(new_string)
