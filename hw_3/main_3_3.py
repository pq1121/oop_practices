from __future__ import annotations

class Robot:

    serial_number: str
    type: str
    current_task: str
    battery_lvl: float
    status: bool

    def __init__(self, serial_number: str, type: str, battery_lvl: float, status=False, current_task=None):
        if not isinstance(serial_number, str):
            raise ValueError('номер должен быть строкой')
        if not isinstance(type, str):
            raise ValueError('тип должен быть строкой')
        if not isinstance(battery_lvl, float):
            raise ValueError('Заряд батареи должен быть числом')
        if battery_lvl > 100 and battery_lvl < 0:
            raise ValueError('Заряд батареи должен быть в пределах от 0 до 100%')

        self.__serial_number = serial_number
        self.__type = type
        self.__current_task = current_task or None
        self.__battery_lvl = battery_lvl
        self.__status = status or False

    def get_serial_number(self):
        return self.__serial_number

    def get_type(self):
        return self.__type

    def get_current_task(self):
        if self.__current_task == None:
            return f"Отдых"
        else:
            return self.__current_task

    def get_battery_lvl(self):
        return self.__battery_lvl

    def set_serial_number(self, value: str):
        if isinstance(value, str):
            self.__serial_number = value
            return True
        else:
            return False

    def set_type(self, value: str):
        if isinstance(value, str):
            self.__type = value
            return True
        else:
            return False

    def set_status(self, value: bool):
        if isinstance(value, bool):
            self.__status = value
            return True
        else:
            return False

    def __str__(self):
        if self.__current_task == None:
            task = 'Отдых'
        else:
            task = self.__current_task
        return (f'Серийный номер: {self.__serial_number}\nТип: {self.__type}\n'
                f'Текущая задача: {task}\n'
                f'Уровень заряда батареи: {self.__battery_lvl}\nСостояние: {self.__status}')

    def add_current_task(self, task: str):
        if isinstance(task, str):
            self.__current_task = task
            return True
        else:
            return False

    def del_current_task(self,):
        self.__current_task = None
        self.__status = False

    def discharge_battery(self, value: float):
        if isinstance(value, float):
            if self.__battery_lvl - value < 0:
                return False
            else:
                self.__battery_lvl -= value
                return True


r = Robot("ffsdfsdf32422ew4r",'киллер',98.00)
print(r)
if r.add_current_task('приготовь лапшу'):
    r.discharge_battery(15.0)
    r.set_status(True)
print(r)
r.del_current_task()
print(r)