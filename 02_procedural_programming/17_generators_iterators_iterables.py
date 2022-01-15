"""
Generators, Iterators and Iterables
Generators and Iterators: you can get their values only once, in for..in loops
or using the next() function. When you access all their values, you cannot
access it again.
"""
import sys
import time

list1 = [1, 2, 3, 4, 5]
# Doint the same thing tha for..in does:
list1 = iter(list1)  # Iterator
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(hasattr(list1, "__iter__"))  # verify iterable
print(hasattr(list1, "__next__"))  # verify iterator
print(sys.getsizeof(list1))  # size is a problem in big size variables


# Generator (lazy evaluation):
def gen(ran: int):
    """Generate values"""
    for v in range(1, ran + 1):
        yield f"Value {v}"
        time.sleep(0.1)


g = gen(10)  # it's an iterator and an interable
for v in g:
    print(v)

# Creating a generator:
l1 = [x for x in range(10000)]
print(type(l1))
l2 = (x for x in range(10000))  # best way to create a generator
print(type(l2))

# Now we have a big difference:
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
for v in l2:
    print(v, end="\r")
