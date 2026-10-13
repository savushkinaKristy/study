dictionary = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")]

def int_to_roman(int_string):
    """
    Преобразует целое число в римскую запись

    Args:
        num (int): Целое положительное число (обычно от 1 до 3999)

    Returns:
        str: Римское представление числа

    Example:
        >>> int_to_roman(42)
        'XLII'
        >>> int_to_roman(2023)
        'MMXXIII'
        """
    result = ""
    for number, symbol in dictionary:
        while int_string >= number: # пока число больше или равно текущ значению, добавляем символ и вычитаем это значение
            result += symbol
            n -= number
        if int_string == 0: # число обнулилось поэтому дальше искать нет смысла
            break
    return result

def roman_to_int(roman_string):
    """
    Преобразует римскую запись числа в целое число.

    Args:
        roman_string (str): Строка, содержащая римское число (например, 'XLII').

    Returns:
        int: Целое число, соответствующее римской записи.

    Example:
        >>> roman_to_int('XLII')
        42
        >>> roman_to_int('MMXXIII')
        2023
    """
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(roman_string)): # идем по индексам строки и потом берем знач текущей буквы
        letter = values[roman_string[i]]
        if i + 1 > len(roman_string) and letter <  values[roman_string[i + 1]]:
            result -= letter
        else:
            result += letter
    return result

print("Число -> Римское:")
print(f"42 -> {int_to_roman(42)}")
print(f"2023 -> {int_to_roman(2023)}")

print("\nРимское -> Число:")
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
for roman in roman_tests:
    print(f"{roman} -> {roman_to_int(roman)}")


