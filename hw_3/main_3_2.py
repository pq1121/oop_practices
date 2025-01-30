from __future__ import annotations

class Employee:

    name: str
    post: str
    department: str
    salary: float
    exp: int
    completed_projects: list

    def __init__(self, name: str, post: str, department: str, salary: int or float, exp: int, completed_projects=None):
        if not isinstance(name, str):
            raise ValueError('Имя сотрудника должно быть строкой')
        if not isinstance(post, str):
            raise ValueError('Должность сотрудника должна быть строкой')
        if not isinstance(department, str):
            raise ValueError('Название отдела должно быть строкой')
        if not isinstance(salary, int or float):
            raise ValueError('Зарплата должна быть числом')
        if salary < 0:
            raise ValueError('Зарплата не может быть отрицательной')
        if not isinstance(exp, int):
            raise ValueError('Стаж работы должен быть числом')
        if not exp >= 0:
            raise ValueError('Стаж работы не может быть отрицательным')

        self.__name = name
        self.__post = post
        self.__department = department
        self.__salary = salary
        self.__exp = exp
        self.__completed_projects = completed_projects or []

    def get_name(self):
        return self.__name

    def get_post(self):
        return self.__post

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def get_exp(self):
        return self.__exp

    def get_completed_projects(self):
        return self.__completed_projects

    def set_post(self, new_post: str):
        if not isinstance(new_post, str):
            raise ValueError('Должность сотрудника должна быть строкой')
        self.__post = new_post

    def set_department(self, new_department: str):
        if not isinstance(new_department, str):
            raise ValueError('Название отдела должно быть строкой')
        self.__department = new_department

    def set_salary(self, value: int or float):
        if not isinstance(value, int or float):
            raise ValueError('Зарплата должна быть числом')
        if value > 0:
            self.__salary = value
        else:
            raise ValueError('Зарплата не может быть отрицательной или равной нулю')

    def set_exp(self, new_exp: int):
        if not isinstance(new_exp, int):
            raise ValueError('Стаж работы должен быть числом')
        if new_exp >= 0:
            self.__exp = new_exp
        else:
            raise ValueError('Стаж работы не может быть отрицательным')

    def __str__(self):
        if len(self.__completed_projects) != 0:
            completed_projects = len(self.__completed_projects)
        else:
            completed_projects = 'Проекты отсутствуют'
        return (f'Сотрудник: {self.__name}\nДолжность: {self.__post}\n'
                f'Отдел: {self.__department}\nЗарплата: {self.__salary}\n'
                f'Стаж работы: {self.__exp}\nВыполненные проекты: {completed_projects}')

    def add_completed_project(self, project):
        if isinstance(project, str):
            self.__completed_projects.append(project)
            return True
        else:
            return False

    def remove_completed_project(self, project):
        if project in self.__completed_projects:
            self.__completed_projects.remove(project)
            return True
        else:
            return False

e = Employee("Алексей",'водитель','главный',2500,3)
print(e)
e.add_completed_project('вывез мусор')
e.add_completed_project('привез товар с тундры')
print(e)