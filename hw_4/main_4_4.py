from __future__ import annotations
from random import randint

class Spell:

    name: str
    description: str
    cost_mp: int
    damage: int

    def __init__(self, name: str, description: str, cost_mp: int, damage: int):
        self.__name = name
        self.__description = description
        self.__cost_mp = cost_mp
        self.__damage = damage

    def get_name(self):
        return self.__name

    def set_name(self, value: str):
        self.__name = value

    def get_cost_mp(self):
        return self.__cost_mp

    def set_cost_mp(self, value: str):
        self.__cost_mp = value

    def get_damage(self):
        return self.__damage

    def set_damage(self, value: str):
        self.__damage = value

    def get_description(self):
        return self.__description

    def set_description(self, value: str):
        self.__description = value

    def __str__(self):
        return (f"Название заклинания:{self.__name}\nРасход маны:{self.__cost_mp}\n"
                f"Описание:{self.__description}")


class HogwartsStudent:

    name: str
    house: str
    hp: int
    mp: int
    spells: list[Spell]


    def __init__(self, name: str, house: str, hp=100, mp=100, spells=None):
        self.__name = name
        self.__house = house
        self.__hp = hp
        self.__mp = mp
        self.__spells = spells or []

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def set_house(self, value: str):
        self.__house = value

    def get_hp(self):
        return self.__hp

    def set_hp(self, value: int):
        self.__hp = value
        if self.__hp <= 0:
            self.__hp = 0
            return False
        else:
            return True

    def get_mp(self):
        return self.__mp

    def set_mp(self, value):
        self.__mp = value
        if self.__mp <= 0:
            self.__mp = 0
            return False
        else:
            return True

    def get_spells(self):
        if len(self.__spells) > 0:
            for i in range(len(self.__spells)):
                print(self.__spells[i])
        else:
            return False

    def learn_spell(self, spell: Spell):
        self.__spells.append(spell)

    def cast_spell(self, target: HogwartsStudent):
        spells_count = len(self.__spells)
        rand_spell = randint(0, spells_count - 1)
        if self.__mp > 0:
            target_new_hp = target.get_hp() - self.__spells[rand_spell].get_damage()
            target.set_hp(target_new_hp)
            new_mp = self.get_mp() - self.__spells[rand_spell].get_cost_mp()
            self.set_mp(new_mp)


    def __str__(self):
        if len(self.__spells) == 0:
            spells = 'Заклинаний нет'
        else:
            spells = ''
            for i in range(0,len(self.__spells)):
                spells += Spell.get_name(self.__spells[i]) + '\n'

        return (f"Имя:{self.__name}\tФакультет:{self.__house}\nМана:{self.__mp}\n"
                f"Заклинания:\n{spells}\n")

class Hogwarts:

    students: HogwartsStudent
    spells: Spell

    def __init__(self, students=None, spells=None):
        self.__students = students or []
        self.__spells = spells or []

    def get_students(self):
        students = ''
        if len(self.__students) > 0:
            for i in range(len(self.__students)):
                students += f"{i+1}. {self.__students[i].get_name()}\n"
            return students

    def get_spell(self):
        spells = ''
        if len(self.__spells) > 0:
            for i in range(len(self.__spells)):
                spells += f"{i+1}. {self.__spells[i].get_name()}\n"
            return spells

    def enroll_student(self, student: HogwartsStudent):
        self.__students.append(student)

    def teach_spell(self, spell: Spell):
        self.__spells.append(spell)

    def simulate_duel(self, student1: HogwartsStudent, student2: HogwartsStudent):
        while (student1.get_mp() > 0 and student1.get_hp() > 0) or (student2.get_mp() > 0 and student2.get_hp() > 0):
            student1.cast_spell(student2)
            student2.cast_spell(student1)
            print(f"{student1.get_name()} hp:{student1.get_hp()}")
            print(f"{student1.get_name()} mp:{student1.get_mp()}")
            print(f"{student2.get_name()} hp:{student2.get_hp()}")
            print(f"{student2.get_name()} mp:{student2.get_mp()}")

s1 = Spell('авада','боевое',40, 50)
s2 = Spell('авада2','боевое',30, 40)

hs1 = HogwartsStudent('first','grif')
hs2 = HogwartsStudent('sec','sliz')

hog = Hogwarts()

hog.enroll_student(hs1)
hog.enroll_student(hs2)
hog.teach_spell(s1)
hog.teach_spell(s2)

hs1.learn_spell(s1)
hs1.learn_spell(s2)
hs2.learn_spell(s1)
hs2.learn_spell(s2)

hog.simulate_duel(hs1,hs2)