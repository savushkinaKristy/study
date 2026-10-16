import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'
goods = {}

def add(items, title, amount, expiration_date = None):
    """
    Добавляет информацию о товаре в словарь items
    Информация включает в себя количество и срок годности (опционально)

    Args:
        items (dict): словарь товаров вида {название: [партии]}
        title (str): название продукта
        amount (Decimal): количество продукта
        expiration_date (str, optional): срок годности в формате '%Y-%m-%d' (по умолчанию None)

    Returns:
        None: функция изменяет словарь на месте

    Example:
        >>> items = {}
        >>> add(items, 'Молоко', Decimal('1.5'), '2023-07-15')
        >>> items
        {'Молоко': [{'amount': Decimal('1.5'), 'expiration_date': datetime.date(2023, 7, 15)}]}
    """
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(
        expiration_date,
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    list.append(
        items[title],
        {"amount": amount, 'expiration_date': expiration_date}
    )

def add_by_note(items, note):
    """
    Принимает два типа данных: перечень товаров items и строку note с информацией о товарах

    Args:
        items (dict): словарь товаров
        note (str): строка вида 'Яйца Фабрики №1 4 2023-07-15'

    Returns:
        None: функция изменяет словарь на месте

    Example:
        >>> items = {}
        >>> add_by_note(items, 'Яйца Фабрики №1 4 2023-07-15')
        >>> items
        {'Яйца Фабрики №1': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}]}
    """
    parts = str.split(note, " ")
    if len(str.split(parts[-1], "-")) == 3:
        expiration_date = parts[-1]
        good_amount = Decimal(parts[-2])
        title = str.join(" ", parts[0:-2])
    else:
        expiration_date = None
        good_amount = Decimal(parts[-1])
        title = str.join(" ", parts[0:-1])
    add(items, title, good_amount, expiration_date)


def find(items, needle):
    """
    Ищет подстроку в элементах списка, возвращает список элементов, которые содержат эту подстроку

    Args:
        items (dict): словарь товаров
        needle (str): строка для поиска (часть названия)

    Returns:
        list: Список названий продуктов, содержащих `needle`

    Example:
        >>> items = {'Молоко': [...], 'Молоток': [...]}
        >>> find(items, 'мол')
        ['Молоко', 'Молоток']
        >>> find(items, 'нет')
        []
    """
    result = []
    for title in items.keys():
        if needle.lower() in title.lower():
            result.append(title)
    return result


def get_amount(items, needle):
    """
    Ищет подстроку в элементах списка, возвращает список элементов, которые содержат эту подстроку

    Args:
        items (dict): словарь товаров
        needle (str): строка для поиска

    Returns:
        Decimal: общее количество найденных продуктов

    Example:
        >>> items = {'Молоко': [{'amount': Decimal('1.5'), ...}, {'amount': Decimal('2'), ...}]}
        >>> get_amount(items, 'мол')
    """
    quantity = Decimal("0")
    found_title = find(items, needle)
    for title in found_title:
        for partia in items[title]:
            quantity += partia["amount"]
    return quantity


def get_expired(items, in_advance_days=0):
    """
    Проверяет продукты на истечение срока годности и делает это с учётом заданного числа дней вперёд,
    а потом — возвращает список продуктов с остаточным количеством

    Args:
        items (dict): словарь товаров
        in_advance_days (int, optional): на сколько дней вперёд проверять(по умолчанию 0)

    Returns:
        list: список кортежей (название, суммарное количество Decimal)

    Example:
        >>> items = {'Яйца': [{'amount': Decimal('2'), 'expiration_date': date(2023, 1, 1)}, {'amount': Decimal('3'), 'expiration_date': date(2023, 1, 2)}]}
        >>> get_expired(items)
        [('Яйца', Decimal('5'))]
    """
    date_today = dt.date.today()
    deadline = date_today + dt.timedelta(days = in_advance_days)
    aggregated = {}
    for title in items:
        for partia in items[title]:
            exp_date = partia["expiration_date"]
            if exp_date is not None and exp_date <= deadline:
                if title not in aggregated:
                    aggregated[title] = Decimal('0')
                aggregated[title] += partia["amount"]
    expired = [(title, amount) for title, amount in aggregated.items()]
    return expired

