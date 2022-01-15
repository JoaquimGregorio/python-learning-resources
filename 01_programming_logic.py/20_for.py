"""
for
range() function: range(start?=0, stop, step?=1)
"""
# text = "Python"
# for c in text:
#     print(c)

for num in range(10, 20, 2):
    print(num)

text = "Python"
new_text = ""
for c in text:
    if c == "t":
        new_text += c.upper()
    elif c == "h":
        new_text += c.upper()
    else:
        new_text += c
print(new_text)
