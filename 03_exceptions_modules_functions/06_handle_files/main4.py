"""
Json to Dict
"""
import json

with open("d1.json", "r") as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Dictionary again
    print(d1_json)
    print(type(d1_json))
