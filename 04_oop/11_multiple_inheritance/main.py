"""
OOP - Multiple Inheritance
"""
from smartphone import Smartphone


class A:
    def speak(self):
        print("Speaking from A...")


class B(A):
    def speak(self):
        print("Speaking from B...")


class C(A):
    def speak(self):
        print("Speaking from C...")


# it will look for the method in the super class
# from the left to right, in this case will find in B,
# otherwise, in C and then in A
class D(B, C):
    pass


d = D()
d.speak()

smartphone = Smartphone("IPhone X11")
smartphone.connect()
smartphone.switch_off()
smartphone.switch_on()
smartphone.connect()
smartphone.connect()
smartphone.connect()
smartphone.switch_off()
smartphone.connect()
smartphone.disconnect()
