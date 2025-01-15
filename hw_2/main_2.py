## Task №1
class Patient:
    name: str
    age: int
    current_sick: str
    def __init__(self, name: str, age: int, current_sick: str):
        self.name = name
        self.age = age
        self.sick = current_sick

    def reg(self, date: str):
        print(f"Пациент {self.name} записан на прием {date}")

    def __str__(self):
        return f"Пациент: {self.name}\nВозраст: {self.age}\nЗаболевание: {self.current_sick}"

## Task №2
class TouristSpot:
    name: str
    country: str
    type: str
    def __init__(self, name: str, country: str, type: str):
        self.name = name
        self.country = country
        self.type = type

    def visit(self, name: str):
        print(f"{name} посетил {self.name} которое находится в {self.country}")

    def __str__(self):
        return f"Туристическое место: {self.name}\nСтрана: {self.country}\nТип: {self.type}"