"""
OOP - Class Attributes (Behavior)
"""


class A:
    vc = 123

    # def __init__(self):
    #    self.vc = 321  # now, instances have this attribute


a1 = A()
a2 = A()

# Doesn't change, just creates an attribute called 'vc'
# directly in the class
a1.vc = 321

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

# changes in all instances
# A.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)
