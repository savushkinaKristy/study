import requests

def get_breeds():
    """
    Получает список всех пород собак из открытого API Dog CEO.

    Returns:
        list[str]: Список строк, содержащий названия всех доступных пород собак.

    Example:
        >>> breeds = get_breeds()
        1. affenpinscher
        2. african
        ...
        >>> print(breeds)
        ['affenpinscher', 'african', 'airedale', ...]
    """
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    dictionary = response.json()
    # делаем список пород из общего списка
    breeds = list(dictionary["message"].keys())
    # делаем нумерованный список
    for number, breed in enumerate(breeds, start=1):
        print(f"{number}. {breed}")
    return breeds

def get_user_breeds():
    """
    Запрашивает у пользователя список пород через консоль.

    Returns:
        list[str]: Список строк с названиями пород, введенными пользователем.

    Example:
        >>> get_user_breeds()
        Введите породы: bulldog, poodle
        ['bulldog', 'poodle']
    """
    result = []
    breeds = input("Введите породы: ")
    # разделяем строку по запятым
    for breed in breeds.split(","):
        # убираем лишние пробелы
        result.append(breed.strip())
    return result

def get_photo(breeds):
    """
    Получает ссылки на случайные фотографии для заданных пород.

    Args:
        breeds (list[str]): Список строк с названиями пород (например, ['boxer', 'pug']).

    Returns:
        list[str]: Список строк со ссылками (URL) на фотографии собак.

    Example:
        >>> get_photo(['boxer'])
        ['https://images.dog.ceo/breeds/boxer/n02108089_1234.jpg']
    """
    photos = []
    for breed in breeds:
        # отправляем GET-запрос для получения случайной фотографии породы
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        dictionary = response.json()
        # добавляем ссылку на фотографию в список
        photos.append(dictionary["message"])
    return photos

