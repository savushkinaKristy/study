from datetime import datetime
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"название: {self.title}, автор: {self.author}, год выпуска: {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        return datetime.now().year - self.year

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(";")
        return cls(title, author, int(year))

    def print_info(self):
        print(self.info())


class Ebook(Book):
    def __init__(self,title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"название: {self.title}, автор: {self.author}, год выпуска: {self.year}, формат: {self.format}"
