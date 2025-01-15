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

# Task №4
class MusicAlbum:

    name: str
    executor: str
    genre: str
    track_list: list

    def __init__(self,name: str, executor: str, genre: str, track_list: list):
        self.name = name
        self.executor = executor
        self.genre = genre
        self.track_list = track_list

    def add_track(self,track: str):
        self.track_list.append(track)

    def del_track(self,track: str):
        if track in self.track_list:
            for i in range(len(self.track_list)):
                if track == self.track_list[i]:
                    self.track_list.pop(i)
                    break
        else:
            print(f"{track} в альбоме {self.name} отсутствует")

    def play(self,track: str):
        if track in self.track_list:
            print("play Music")
        else:
            print(f"{track} в альбоме {self.name} отсутствует, выберите другой трек")