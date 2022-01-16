"""
Task List
Add, List, Undo, Redo
"""


def add_task(task: str, todo_list: list):
    todo_list.append(task)
    print("Task added successfully!")


def show_todo_list(todo_list: list):
    print(f"There are {len(todo_list)} tasks:")
    for i, task in enumerate(todo_list, start=1):
        i = f"{i}" if len(str(i)) > 1 else f"0{i}"
        print(f"\t{i} - {task}")


def undo_task_list(task_list: list, redo_list: list):
    if len(todo_list) == 0:
        print("There's nothing to undo!")
        return
    redo_list.append(task_list.pop())
    print("Undone!")


def redo_task_list(redo_list: list, task_list: list):
    if len(redo_list) == 0:
        print("There's nothing to redo!")
        return
    task_list.append(redo_list.pop())
    print("Redone!")


todo_list = []
redo_list = []

while True:
    print("What do you wanna do?")
    action = input("(A)dd, L(ist), (U)ndo or (R)edo? ").upper()
    if len(action) > 1:
        print("Please type only one letter!")
        continue
    elif action == "A":
        task = input("Type your task: ")
        add_task(task, todo_list)
        continue
    elif action == "L":
        show_todo_list(todo_list)
        continue
    elif action == "U":
        undo_task_list(todo_list, redo_list)
        continue
    elif action == "R":
        redo_task_list(redo_list, todo_list)
        continue
    else:
        print("Type a valid letter!")
