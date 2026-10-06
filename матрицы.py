def det_2x2(a, b, c, d):
    """Определитель матрицы 2x2: a*d - b*c"""
    return a * d - b * c


def det_sarrus(matrix):
    """
    Определитель 3x3 по правилу Саррюса (диагонали).
    matrix = [[a, b, c], [d, e, f], [g, h, i]]
    """
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    # Плюсы: диагонали сверху-вниз
    plus = a * e * i + b * f * g + c * d * h
    # Минусы: диагонали снизу-вверх
    minus = c * e * g + a * f * h + b * d * i

    return plus - minus


def det_by_first_row(matrix):
    """
    Определитель 3x3 разложением по первой строке.
    Знаки: + - +
    """
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    return (
            a * det_2x2(e, f, h, i)
            - b * det_2x2(d, f, g, i)
            + c * det_2x2(d, e, g, h)
    )


def main():
    print("Введите матрицу 3x3 (9 чисел через пробел):")
    print("Пример: 2 1 3 0 4 5 1 2 6")

    numbers = list(map(float, input().split()))

    if len(numbers) != 9:
        print("Ошибка: нужно ровно 9 чисел!")
        return

    matrix = [numbers[0:3], numbers[3:6], numbers[6:9]]

    print("\nВаша матрица:")
    for row in matrix:
        print(row)

    result_sarrus = det_sarrus(matrix)
    result_row = det_by_first_row(matrix)

    print(f"\nОпределитель (Саррюс):       {result_sarrus}")
    print(f"Определитель (по строке):    {result_row}")

    if result_sarrus == result_row:
        print("Оба способа дали одинаковый ответ!")
    else:
        print("Ответы не совпали — где-то ошибка в коде.")


if __name__ == "__main__":
    main()