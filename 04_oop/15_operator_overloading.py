"""
Operator    Method          Operation
------------------------------------------------------
+           __add__         Add
-           __sub__         subtraction
*           __mul__         Multiplication
/           __div__         Division
//          __floordiv__    Integer division
%           __mod__         Modulus
**          __pow__         Power
+           __pos__         Positive
-           __neg__         Negative
<           __lt__          Less than
>           __gt__          Greater than
<=          __le__          Less or equals to
>=          __ge__          Greater or equal to
==          __eq__          Equal to
!=          __ne__          Different from
<<          __lshift__      Bitwase left shift
>>          __rshift__      Bitwase right shift
&           __and__         Bitwase AND
|           __or__          Bitwase OR
^           __xor__         Bitwase XOR (exclusive OR)
~           __inv__         Bitwase NOT

Changing class operators behavior
"""


class Rectangle:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    # change the class output when print on console
    def __repr__(self) -> str:
        return f"<class 'Rectangle({self.x}, {self.y})'>"

    # `other` is the other object to be added
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Rectangle(new_x, new_y)

    def __lt__(self, other) -> bool:
        a1 = self.get_area()
        a2 = other.get_area()

        return a1 < a2

    def __gt__(self, other) -> bool:
        a1 = self.get_area()
        a2 = other.get_area()

        return a1 > a2

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(10, 30)
print(r1 + r2)
print(r1 > r3)
print(r1 < r3)
print(r1 == r2)
