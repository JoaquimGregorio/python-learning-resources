"""
Functions
"""


def greeting(msg: str = "Hello", name: str = "user") -> str:
    """Prints and returns some greeting."""
    print(msg, name)

    return f"{msg} {name}"


greeting()
greeting("Hi", "Joaquim")
greeting(name="Marcos", msg="Nice to meet you")
