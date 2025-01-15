## Task №1
class Patient:
    name: str
    age: int
    current_sick: str
    def __init__(self,name: str, age: int,current_sick: str):
        self.name = name
        self.age = age
        self.sick = current_sick

    def reg(self,date: str):
        print(f"Пациент {self.name} записан на прием {date}")

    def __str__(self):
        return f"Пациент: {self.name}\nВозраст: {self.age}\nЗаболевание: {self.current_sick}"