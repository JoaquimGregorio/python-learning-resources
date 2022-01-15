"""
String manipulation
* String indexes (supports either positive and negative indexes)
* String slicing [beginning:end:pass]
* Built-in functions len, abs, type, print, etc...
These functions can be used directly in each type
"""
text = "Python_s2"  # [012345678] and -[987654321] as indexes
# print(text[-2])

url = "www.voidlinux.org/"

print(url[4:-1])  # slicing

new_text = text[:6]
new_text_2 = text[7:]
print(new_text, new_text_2)
print(text[:-2])

# [beginning:end:pass]

print(text[::2])  # jumping 2 characters in all the string
print(text[0:6:2])  # from 0 till 6 jumping 2 characters (ignoring one character)

for char in text:
    print(char)
