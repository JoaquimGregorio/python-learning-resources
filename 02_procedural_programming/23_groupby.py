"""
Groupby
"""
from itertools import groupby, tee

students = [
    {"name": "Joaquim", "grade": "A"},
    {"name": "João", "grade": "B"},
    {"name": "Maria", "grade": "B"},
    {"name": "Márcia", "grade": "F"},
    {"name": "Luiz", "grade": "D"},
    {"name": "Mario", "grade": "A"},
    {"name": "Carlos", "grade": "A"},
    {"name": "Geraldo", "grade": "A"},
    {"name": "Ronaldo", "grade": "B"},
    {"name": "Cristina", "grade": "C"},
]
order = lambda item: item["grade"]
students.sort(key=order)
# you need to order the valures before use groupby
ordered_students = groupby(students, order)

for group, students_group in ordered_students:
    print(f"Group: {group}")
    new_group, new_group2 = tee(students_group)  # make a copy because it is an iterator
    length = len(list(new_group))
    print(f"\tThere is {length} students in this group.")
    for student in new_group2:
        print(f"\t{student}")
