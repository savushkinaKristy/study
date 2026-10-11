ru_alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en_alfavit = "abcdefghijklmnopqrstuvwxyz"
def detect_language(text):
    """
    Определяет язык введённого текста (русский или английский)

    Args:
        text (str): Текст для анализа

    Returns:
        str: "ru" — если текст на русском, "en" — если на английском, "unknown" — если буквы не найдены

    Example:
        >>> detect_language("Привет, мир!")
        'ru'
        >>> detect_language("Hello, world!")
        'en'
        >>> detect_language("12345")
        'unknown'
    """

    for bukva in text:
        bukva = bukva.lower()
        if bukva not in ru_alfavit and bukva not in en_alfavit: # если символа нет в алфавитах, пропускаем его
            continue
        if bukva in ru_alfavit:
            return "ru"
        elif bukva in en_alfavit:
            return "en"
    return "unknow"
def cipher(text, shift, mode):
    """
    Шифрует или дешифрует текст шифром Цезаря.

    Args:
        text (str): Исходный текст.
        shift (int): Величина сдвига (целое число).
        mode (str): Режим работы: 'encrypt' для шифрования, 'decrypt' для дешифрования.

    Returns:
        str: Преобразованный текст.

    Example:
        >>> cipher("Привет", 3, "encrypt")
        'Тулезх'
        >>> cipher("Тулезх", 3, "decrypt")
        'Привет'
        >>> cipher("Hello", 2, "encrypt")
        'Jgnnq'
    """

    # определяем язык текста
    language = detect_language(text)
    if language == "ru":
        alfavit = ru_alfavit
    elif language == "en":
        alfavit = en_alfavit
    else:
        return text # если язык неизвестен, возвращаем сам текст

    # учитываем, что при дешифровке сдвиг идет в обратную сторону
    if mode == "decrypt":
        shift = -shift

    result=[]
    for bukva in text:
        if bukva.isalpha(): # проверяем, что это правда буква
            is_upper = bukva.isupper() # запоминаем, что буква была заглавной
            low_bukva = bukva.lower() # работаем с нижним регистром

            index = alfavit.index(low_bukva) # находим индекс буквы
            new_index = (index + shift) % len(alfavit) # это если мы уйдем за пределы алфавита
            new_bukva = alfavit[new_index]

            # если буква была заглавной, делаем ее снова такой
            if is_upper:
                new_bukva=new_bukva.upper()
            result.append(new_bukva)
        else: # если это не буква, то просто добавляем без изменений
            result.append(bukva)
    return "".join(result)

text=input("Введите текст: ")
shift=int(input("Введите сдвиг: "))

encrypted=cipher(text, shift, mode="encrypt")
print(f"Зашифровано: {encrypted}")

decrypted=cipher(encrypted, shift, mode="decrypt")
print(f"Расшифровано: {decrypted}")



