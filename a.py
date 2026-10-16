import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {}


def add(items, title, amount, expiration_date=None):
    """
    Добавляет партию продукта в холодильник.

    Args:
        items (dict): Словарь товаров.
        title (str): Название продукта.
        amount (Decimal): Количество продукта.
        expiration_date (str, optional): Дата в формате '%Y-%m-%d'.

    Returns:
        None: Функция изменяет словарь на месте.
    """
    # Если продукта нет — создаём для него пустой список
    if title not in items:
        items[title] = []

    # Если дата передана строкой — преобразуем в тип date
    expiration_date = (
        dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
        if expiration_date
        else expiration_date
    )

    # Добавляем партию в список
    items[title].append(
        {'amount': amount, 'expiration_date': expiration_date}
    )


def add_by_note(items, note):
    """
    Добавляет продукт, разбирая текстовую заметку.

    Args:
        items (dict): Словарь товаров.
        note (str): Строка вида 'Яйца Фабрики №1 4 2023-07-15'.

    Returns:
        None: Функция изменяет словарь на месте.
    """
    parts = note.split(' ')

    # Если последняя часть содержит дату (три числа через дефис)
    if len(parts[-1].split('-')) == 3:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


if __name__ == "__main__":
    add(goods, 'Молоко', Decimal('1.5'), '2023-07-15')
    add(goods, 'Хлеб', Decimal('2'))
    add_by_note(goods, 'Яйца Фабрики №1 4 2023-07-15')
    add_by_note(goods, 'Сыр 1.5')

    for name, batches in goods.items():
        print(name, '->', batches)