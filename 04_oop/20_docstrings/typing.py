"""Module's documentation

This module does nothing since it's just an example.
Typing - https://docs.python.org/3/library/typing.html
"""
var1: str = "Some variable"


def func(p1: float, p2: str, p3: dict) -> float:
    return 18.9


# Union types:


def func2(n1: int | float, n2: int | float) -> list | dict:  # Union[list, dict]
    if n1 < n2:
        return []
    else:
        return {}


# type alias
ListOrDict = list | dict


def func3(n1: int | float, n2: int | float) -> ListOrDict:
    if n1 < n2:
        return []
    else:
        return {}
