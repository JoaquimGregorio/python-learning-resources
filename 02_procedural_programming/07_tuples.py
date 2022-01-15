"""
Tuples
In tuples we cannot insert or remove elements and we
cannot change their values. That's why tuples are
different from lists
"""
t1 = (1,)  # or just 't1 = 1,'
t2 = ()
t3 = (1, 2, 3, "a", "b", "c")
t4 = 6, 7, 8, "d", "e", "f"
t5 = t3 + t4
t6 = ("a", 1) * 4  # repeat '"a", 1' four times

print(t6)

t7 = ("a", "b", "c")
t7 = list(t7)  # you can create another variable just for it
t7.append("d")
t7 = tuple(t7)

print(t7)

t8 = (1, 2, 3)
item = (4,)  # it can be multiple items
t8 += item

print(t8)
