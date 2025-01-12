# Task №1
class Animal:

    name: str
    type: str
    agr: int

    def __init__(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age

    def sound(self):
        print('sound')

    def info(self):
        print(f"name: {self.name}, type: {self.type}, age: {self.age}")

    def __add__(self, other):
        self.name += other.name
        self.type += other.type
        self.age += other.age
