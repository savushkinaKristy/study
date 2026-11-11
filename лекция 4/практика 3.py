import requests

team = []

def get_pokemon(name):
    """
    Получает информацию о покемоне из API PokeAPI по его имени.

    Args:
        name (str): Имя покемона (например, 'pikachu').

    Returns:
        dict: Словарь с полной информацией о покемоне, если он найден.
        None: Если покемон с таким именем не существует (код ответа не 200).
    """
    # убираем лишние пробелы и делаем нижний регистр
    name = name.lower().strip()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    res = response.json()
    # если покемон есть, возвращаем всю инфу о нем
    if response.status_code == 200:
        return res
    else:
        return None

def add_pokemon(name):
    """
    Добавляет покемона в текущую команду.
    Сначала проверяет, существует ли такой покемон в API,
    а затем проверяет, нет ли его уже в команде, чтобы избежать дубликатов.

    Args:
        name (str): Имя покемона, которого нужно добавить.

    Returns:
        None: Функция ничего не возвращает, а выводит результат в консоль
    """
    information = get_pokemon(name)
    # если покемон существует, будем добавлять в команду
    if information is not None:
        for member in team:
            # проверяем есть ли покемон уже в команде
            if information["name"] == member["name"]:
                print("Покемон уже есть в команде")
                return  # завершаем функцию
        team.append(information)
        print("Покемон успешно добавлен!")
    else:
        print("Покемон не найден")

def remove_pokemon(name):
    """
    Удаляет покемона из команды.

    Args:
        name (str): Имя покемона, которого нужно удалить.

    Returns:
        None: Функция ничего не возвращает, а выводит результат в консоль
    """
    name = name.lower().strip()
    for member in team:
        # смотрим, есть ли вообще пикачу в команде, если да - удаляем
        if name == member["name"]:
            team.remove(member)
            print("Покемон удален")
            return
    print("Покемон не найден")

def viewing_pokemon():
    """
    Показывает всю информацию о членах команды.
    Если команда пуста, выводит соответствующее сообщение.

    Args:
        Нет аргументов.

    Returns:
        None: Выводит информацию в консоль.
    """
    if not team:
        print("Команда пуста")
        return
    for member in team:
        print(member)

def battle_pokemon(name_1, name_2):
    """
    Устраивает тренировачный бой между двумя выбранными покемонами.

    Args:
        name_1 (str): имя первого покемона.
        name_2 (str): имя второго покемона.

    Returns:
        None: Выводит того, кто победил
    """
    name_1 = name_1.lower().strip()
    name_2 = name_2.lower().strip()
    # создаём переменные для хранения покемонов
    pokemon_1 = None
    pokemon_2 = None
    for member in team:
        if name_1 == member["name"]:
            pokemon_1 = member
        if name_2 == member["name"]:
            pokemon_2 = member
    if pokemon_1 is None or pokemon_2 is None:
        print("Какой то покемон не найден в команде")
        return
    # определяем их силу
    power_1 = 0
    power_2 = 0
    for stat in pokemon_1["stats"]:
        power_1 += stat["base_stat"]
    for stat in pokemon_2["stats"]:
        power_2 += stat["base_stat"]
    # определяем кто сильнее
    if power_1 > power_2:
        print("Первый покемон сильнее и он победил")
    elif power_2 > power_1:
        print("Второй покемон сильнее и он победил")
    else:
        print("Ничья")

while True:
    print("1. Добавить покемона")
    print("2. Удалить покемона")
    print("3. Показать команду")
    print("4. Тренировочный бой")
    print("0. Выйти")

    choice = input("Выберите действие: ")

    if choice == "0":
        print("Пока")
        break

    elif choice == "1":
        name = input("Введите имя покемона: ")
        add_pokemon(name)

    elif choice == "2":
        name = input("Введите имя покемона: ")
        remove_pokemon(name)

    elif choice == "3":
        viewing_pokemon()

    elif choice == "4":
        name_1 = input("Введите имя первого покемона: ")
        name_2 = input("Введите имя второго покемона: ")
        battle_pokemon(name_1, name_2)

    else:
        print("Неверный пункт меню")

