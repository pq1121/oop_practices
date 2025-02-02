from __future__ import annotations


class Genre:
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description


class Book:
    title: str
    author: str
    year: int
    id: int
    genre: list[Genre]

    def __init__(self,title: str, author: str, year: int, id: int, genre=None):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = id
        self.__genre = genre or []

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_id(self):
        return self.__id

    def get_genre(self):
        genre = ''
        if len(self.__genre) == 0:
            return "Жанр отсутствует"
        else:
            for i in range(0, len(self.__genre)):
                genre += f"{i+1}.{self.__genre[i].get_name()}\n"
        return genre

    def add_genre(self, genre: Genre):
        self.__genre.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genre:
            self.__genre.remove(genre)

class ContactInfo:
    type: str
    value: str

    def __init__(self, type: str, value: str):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

class Employee:
    name: str
    position: str
    id: int
    contact_info: list[ContactInfo]

    def __init__(self, name: str, position: str, id: int):
        self.__name = name
        self.__position = position
        self.__id = id
        self.__contact_info = []

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return f"type: {self.__contact_info[0].get_type()}, value: {self.__contact_info[0].get_value()}"

    def add_contact_info(self, type: str, value: str):
        self.__contact_info.append(ContactInfo(type, value))


class Library:
    name: str
    address: str
    books: list[Book]
    Empoloyees: list[Employee]

    def __int__(self, name: str, address=None):
        self.__name = name
        self.__address = address
        self.__books = []
        self.__Employees = []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_name(self, name: str):
        self.__name = name

    def set_address(self, address: str):
        self.__address = address

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, book: Book):
        self.__books.remove(book)

    def add_employee(self, employee: Employee):
        self.__Employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.__Employees.remove(employee)