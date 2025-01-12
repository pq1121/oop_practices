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

# Task №3
class PassengerPlane:
    manufacturer: str
    model: str
    capacity_passenger: int
    current_height: float
    current_speed: float
    def __init__(self,manufacturer: str, model: str, current_height: float, current_speed: float):
        self.manufacturer = manufacturer
        self.model = model
        self.current_height = current_height
        self.current_speed = current_speed

    def takeoff(self):
        print("Самолет взлетел!")

    def landing(self):
        print("Самолет приземлился!")

    def change_height(self,height: float):
        self.current_height = height

    def change_speed(self, speed: float):
        self.current_speed = speed

    def __add__(self, other):
        self.manufacturer += other.manufacturer
        self.model += other.model
        self.current_height += other.current_height
        self.current_speed += other.current_speed