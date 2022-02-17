from datetime import datetime


class Person:
    current_year = int(datetime.strftime(datetime.now(), "%Y"))  # class variable

    def __init__(
        self, name: str, age: int, eating: bool = False, speaking: bool = False
    ):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, subject: str):
        if self.eating:
            print(f"{self.name} cannot speak while eat.")
            return

        if self.speaking:
            print(f"{self.name} is already speaking.")
            return

        self.speaking = True
        print(f"{self.name} is speaking {subject}.")

    def stop_speaking(self):
        if not self.speaking:
            print(f"{self.name} isn`t speaking.")
            return

        self.speaking = False
        print(f"{self.name} stop speaking.")

    def eat(self, food: str):
        if self.eating:
            print(f"{self.name} is already eating.")
            return

        if self.speaking:
            print(f"{self.name} cannot eat while speak")
            return

        self.eating = True
        print(f"{self.name} is eating {food.lower()}.")

    def stop_eating(self):
        if not self.eating:
            print(f"{self.name} isn't eating.")
            return

        self.eating = False
        print(f"{self.name} stop eating.")

    def get_year_of_birth(self):
        return self.current_year - self.age
