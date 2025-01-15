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