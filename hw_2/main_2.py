## Task №1
class Patient:
    first_name: str
    sec_name: str
    last_name: str
    age: int
    current_sick: str
    @property
    def (self):
        return 
    
    @.setter
    def (self, value):
        pass
    def __init__(self, first_name: str, sec_name: str, last_name: str, age: int, current_sick: str):
        self.__first_name = first_name
        self.__sec_name = sec_name
        self.__last_name = last_name
        self.__age = age
        self.__sick = current_sick

    def reg(self, date: str):
        print(f"Пациент {self.__sec_name} {self.__first_name} {self.__last_name} записан на прием {date}")

    def __str__(self):
        return f"Пациент: {self.__sec_name} {self.__first_name} {self.__last_name}\nВозраст: {self.age}\nЗаболевание: {self.current_sick}"

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

## Task №3
class ModelWindow:
    title: str
    coord_left_upper_corner: list
    size_width: int
    size_height: int
    color_window: str
    visible: bool
    frame: bool
    window_width = 1960
    window_height = 1080

    def __init__(self, title: str, coord_left_upper_corner: list, size_width: int,
                 size_height: int, color_window: str = "gray", visible: bool = True, frame: bool = True):
        self.title = title
        self.coord_left_upper_corner = coord_left_upper_corner
        self.size_width = size_width
        self.size_height = size_height
        self.color_window = color_window
        self.visible = visible
        self.frame = frame

    def move_horizontal(self,size: int):
        if self.size_width + size <= ModelWindow.window_width:
            self.coord_left_upper_corner[0] = size
        else:
            print(f"Передвинуть окно по горизонтали не возможно")

    def move_vertical(self, size: int):
        if self.size_height + size <= ModelWindow.window_height:
            self.coord_left_upper_corner[1] = size
        else:
            print(f"Передвинуть окно по вертикали не возможно")

    def change_size_window(self, size: list[int]):
        """

        :param size: size[0] -> new width size[1] -> new height
        :return:
        """
        if size[0] > 0 and size[0] <= ModelWindow.window_width:
            self.size_width = size[0]
        if size[1] > 0 and size[1] <= ModelWindow.window_height:
            self.size_height = size[1]

    def new_color(self, color: str):
        self.color_window = color

    def change_visible(self, param: bool):
        self.visible = param

    def change_frame(self, param: bool):
        self.frame = param

    def output_state(self):
        print("Состояние")
        print("Видимое" if self.visible else "Невидимое")
        print("С рамкой" if self.frame else "без рамки")

    def __str__(self):
        return (f"Заголовок :{self.title}\nКоординаты левого верхнего угла: {self.coord_left_upper_corner}\n"
                f"Цвет окна: {self.color_window}\nРазмер по горизонтали: {self.size_width}\n"
                f"Размер по вертикали: {self.size_height}")

# Task №8
class Time:

    hour: int
    min: int
    sec: int

    def __init__(self, hour: int, min: int, sec: int):
        self.hour = hour
        self.min = min
        self.sec = sec

    def correction(self):
        if self.sec > 59:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        if self.min > 59:
            self.hour += self.min // 60
            self.min = self.min % 60

    def __add__(self, other):
        new_hour = self.hour + other.hour
        new_min = self.min + other.min
        new_sec = self.sec + other.sec
        return Time(new_hour, new_min, new_sec)

    def __sub__(self, other):
        if self.hour < other.hour and self.hour != other.hour:
            return False
        else:
            if self.sec < other.sec and self.sec != other.sec:
                self.min -= 1
                new_sec = self.sec + 60 - other.sec
            else:
                new_sec = self.sec - other.sec
            if self.min < other.min and self.min != other.min:
                self.hour -= 1
                new_min = self.min + 60 - other.min
                new_hour = self.hour - other.hour
            else:
                new_min = self.min - other.min
                new_hour = self.hour - other.hour
        return Time(new_hour, new_min, new_sec)

    def __mul__(self, other):
        return Time(self.hour * other, self.min * other, self.sec * other)

    def __str__(self):
        if self.hour // 10 == 0:
            buff_hour = "0" + str(self.hour)
        else:
            buff_hour = self.hour
        if self.min // 10 == 0:
            buff_min = int("0" + str(self.min))
        else:
            buff_min = self.min
        if self.sec // 10 == 0:
            buff_sec = int("0" + str(self.sec))
        else:
            buff_sec = self.sec
        return f"{buff_hour}:{buff_min}:{buff_sec}"