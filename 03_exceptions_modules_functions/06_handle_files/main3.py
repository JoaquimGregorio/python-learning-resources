"""
Json
"""
import json

d1 = {
    "Person 1": {"name": "Joaquim", "age": 18},
    "Person 2": {"name": "Marcos", "age": 23},
}

d1_json = json.dumps(d1, indent=True)

with open("d1.json", "w+") as file:
    file.write(d1_json)
