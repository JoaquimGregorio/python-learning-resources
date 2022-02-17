"""
OOP - Polymorphism, the same class properties with different behaviors
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def speak(self, msg: str):
        pass


class B(A):
    def speak(self, msg: str):
        print(f"B is speaking {msg}")


class C(A):
    def speak(self, msg: str):
        print(f"C is speaking {msg}")


# C `speak` method differs from B `speak` method,
# but both has the same class signature provided
# by class A.

b = B()
c = C()
b.speak("Some subject")
c.speak("Another subject")
