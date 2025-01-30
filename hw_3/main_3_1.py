from __future__ import annotations
class Spell:

    name: str
    complexity: int
    type: str
    description: str

    def __init__(self, name: str, complexity: int, type: str, description: str):
        if not isinstance(name, str):
            raise ValueError('Название заклинания должно быть строкой')
        if not isinstance(complexity, int):
            raise ValueError('Уровень сложности должен быть целым числом')
        if not 1 <= complexity <= 10:
            raise ValueError('Уровень сложности должен быть от 1 до 10')
        if not isinstance(type, str):
            raise ValueError('Тип должен быть строкой')
        if not isinstance(description, str):
            raise ValueError('Описание должно быть строкой')
        self.__name = name
        self.__complexity = complexity
        self.__type = type
        self.__description = description

    def get_name(self):
        return self.__name

    def set_name(self, value: str):
        self.__name = value

    def get_complexity(self):
        return self.__complexity

    def set_complexity(self, value: int):
        if value >= 1 and value <= 10:
            self.__complexity = value
        else:
            print("Сложность заклинания может быть от 1 до 10")
            return False

    def get_type(self):
        return self.__type

    def set_type(self, value: str):
        self.__type = value

    def get_description(self):
        return self.__description

    def set_description(self, value: str):
        self.__description = value

    def __str__(self):
        return (f"Название заклинания:{self.__name}\nУровень сложности:{self.__complexity}\n"
                f"Тип:{self.__type}\nОписание:{self.__description}")

    name = property(get_name, set_name)
    complexity = property(get_complexity,set_complexity)
    type = property(get_type,set_type)
    description = property(get_description, set_description)

class Wizard:

    name: str
    faculty: str
    magic_level: float
    spells: list[Spell]
    status: str

    def __init__(self, name: str, faculty: str, magic_level: float, status: str, spells=None):
        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой')
        if not isinstance(faculty, str):
            raise ValueError('Название факультета должно быть строкой')
        if not isinstance(magic_level, int):
            raise ValueError('Уровень магической силы должно быть число')
        if not magic_level >= 0:
            raise ValueError('Уровень магической силы не может быть отрицательным')
        if not isinstance(status, str):
            raise isinstance('Статус волшебника должно быть строкой')
        self.__name = name
        self.__faculty = faculty
        self.__magic_level = magic_level
        self.__status = status
        self.__spells = spells or []

    def get_name(self):
        return self.__name

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, value: str):
        self.__faculty = value

    def get_magic_level(self):
        return self.__magic_level

    def set_magic_level(self, value: str):
        self.__magic_level = value

    def get_spells(self):
        if len(self.__spells) > 0:
            for i in range(len(self.__spells)):
                print(self.__spells[i])
        else:
            return False

    def get_status(self):
        return self.__status

    def set_status(self, value: str):
        self.__status = value

    def add_spell(self, spell: Spell):
        if isinstance(spell, Spell):
            self.__spells.append(spell)
            print("Добавлено заклинание")
        else:
            raise ValueError("Не верный формат заклинания")

    def remove_spell(self, spell: Spell):
        if isinstance(spell, Spell):
            if spell in self.__spells:
                self.__spells.remove(spell)
                return True
            else:
                return False

        else:
            raise ValueError("Не верное заклинание")

    def increase_magic_level(self, amount: float):
        if amount > 0:
            self.__magic_level += amount
            print("Вы чувствуете увеличение магической силы")
        else:
            return False

    def __str__(self):
        if len(self.__spells) == 0:
            spells = 'Заклинаний нет'
        else:
            spells = ''
            for i in range(0,len(self.__spells)):
                spells += Spell.get_name(self.__spells[i]) + '\n'

        return (f"Имя:{self.__name}\tФакультет:{self.__faculty}\nУровень магической силы:{self.__magic_level}\n"
                f"Текущий статус:{self.__status}\nЗаклинания:\n{spells}\n")

s = Spell('Бомбарда', 5, 'Боевое', 'заклинание, взрыва препятствия')
s1 = Spell('Бомбарда Максимум', 9, 'Боевое', 'заклинание, взрыва препятствия')
w = Wizard('Alex', 'Слизорен', 564,'в Хогвартсе')
print(w)
w.add_spell(s)
w.add_spell(s1)
print(w)