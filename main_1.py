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

# Task №2
class Book:

    name: str
    author: str
    pages: int

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def open_page(self, page: int):
        if page <= self.pages:
            print(f"Открыта станица {page} в книге {self.name}")
        else:
            print(f"Стрницы {page} в книге {self.name} нету")

    def info(self):
        print(f"name: {self.name}, author: {self.author}, pages: {self.pages}")

    def __add__(self, other):
        self.name += other.name
        self.author += other.author
        self.pages += other.pages