class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__

    def speak(self):
        print(f"{self.class_name} is speaking...")


class Customer(Person):
    def buy(self):
        print(f"{self.class_name} is shopping...")

    def speak(self):
        print("speak method from Customer class.")


class Student(Person):
    def study(self):
        print(f"{self.class_name} is studying...")


class VIPCustomer(Customer):
    def __init__(self, name: str, lastname: str, age: int):
        super().__init__(name, age)  # but we can also override the constructor
        # we can also specify the super class:
        # Person.__init__(self, name, age)
        self.lastname = lastname

    # Overriding:
    def speak(self):
        # specifying super class to call `speak` method:
        Person.speak(self)
        Customer.speak(self)

        # `super` will call the method from the first super class:
        # super().speak()

        print(f"{self.name} {self.lastname} is speaking from {self.class_name}...")
