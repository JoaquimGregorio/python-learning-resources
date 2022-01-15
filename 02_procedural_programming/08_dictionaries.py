"""
Dictionaries
"""
d1 = {"key": "key value", "key": "key value 2", "key": "key real value"}
d1["new_key"] = "new_key value"
print(d1)

d2 = dict(
    key1="key1 value",
    key2="key2 value",
)

## Accept immutable types as keys:
d3 = {"str": "value", 123: "other value", (1, 2, 3): "tuple as key"}

## Deleting a key:
del d3["str"]

print(d3)

## Verify if a KEY exists:
print("str" in d3)  # or '"str" in d3.keys()'
## Verify if a VALUE exists:
print("other value" in d3.values())
## Verify number of paris (key:value)
print(len(d3))


# Looping:
d4 = {
    "key1": "key1 value",
    "key2": "key2 value",
    "key3": "key3 value",
    "key4": "key4 value",
}

for key in d4:
    print(key, d4[key])

for value in d4.values():
    print(value)

for key_value in d4.items():
    print(key_value)  # tuples

for k, v in d4.items():
    print(k, v)
