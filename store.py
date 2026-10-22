# Импортируйте нужную библиотеку.
from datetime import datetime

class Store:
    def __init__(self, address):
        self.address: str = address

    def is_open(self, date) -> bool:
        # Метод is_open() в родительском классе всегда возвращает False,
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        return False

    def get_info(self, text_date) -> str:
        date_object = datetime.strptime(text_date, '%d.%m.%Y')

        # Передайте в метод is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {text_date} {info}'


class MiniStore(Store):
    # Переопределите метод is_open().
    # Мини-маркеты работают только по будним дням (пн-пт)
    def is_open(self, date: datetime) -> bool:
        return date.weekday() < 5

class WeekendStore(Store):
    def is_open(self, date: datetime) -> bool:
        return date.weekday() > 4


class NonStopStore(Store):
    # Магазины non-stop работают всегда
    # Переопределите метод is_open().
    def is_open(self, date: datetime) -> bool:
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))