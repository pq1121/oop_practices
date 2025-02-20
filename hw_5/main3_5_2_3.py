from __future__ import annotations
from abc import ABC, abstractmethod


class Airline:

    def __init__(self, name: str, airports: list[Airport], employees: list[Employee]):

        self.__name = name
        self.__airports = airports or []
        self.__employees = employees or []


class Airport:

    def __init__(self, name: str, address: str, employees: list[Employee], transports: list[ATransport],
                 passengers: list[Passenger]):

        self.__name = name
        self.__address = address
        self.__employees = employees or []
        self.__transports = transports or []
        self.__passengers = passengers or []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_name(self, name: str):
        self.__name = name

    def set_address(self, address: str):
        self.__address = address

    def fligth(self):
        return "Пора в рейс"


class ATransport(ABC):

    def __init__(self, name: str, description: str):

        self.__name = name
        self.__description = description

    @abstractmethod
    def move(self): pass


class Airplane(ATransport):

    def __init__(self, name, description, type: str):
        super().__init__(name, description)
        self.__type = type


class Bus(ATransport):

    def __init__(self, name, description, type: str):
        super().__init__(name, description)
        self.__type = type


class Employee:

    def __init__(self, name: str, age: int, posts: list[Post]):

        self.__name = name
        self.__age = age
        self.__posts = posts or []

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: str):
        self.__age = age

    def work(self):
        return "Работаем"


class Post:

    def __init__(self, title: str, salary: int):

        self.__title = title
        self.__salary = salary

class Passenger:

    def __init__(self, name: str, data: int, ticket_ID: int):

        self.__name = name
        self.__data = data
        self.__ticket_ID = ticket_ID

    def get_name(self):
        return self.__name

    def get_dataself):
        return self.__data

    def set_name(self, name: str):
        self.__name = name

    def set_data(self, data: str):
        self.__data = data
