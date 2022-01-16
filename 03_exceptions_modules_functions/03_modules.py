"""
Default python modules
https://docs.python.org/3/py-modindex.html
"""
# import sys
# from sys import platform
# from sys import platform as so
# print(so)
# NOTE: the following way can be confused:
# from random import *
import random as rand

for i in range(10):
    print(rand.randint(-1, 10), rand.random())
