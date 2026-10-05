import random


def roll_dice(sides=6, count=1):
    """Бросает `count` кубиков с `sides` гранями и возвращает список результатов."""
    return [random.randint(1, sides) for _ in range(count)]


def main():
    print("🎲 Симулятор броска кубиков")
    print("Нажми Enter, чтобы бросить кубик, или введи 'q' для выхода.\n")

    total_rolls = 0

    while True:
        command = input("Бросок! (Enter / q): ").strip().lower()

        if command == 'q':
            print(f"\nВсего бросков: {total_rolls}. Пока!")
            break

        # Бросаем два стандартных шестигранных кубика
        results = roll_dice(sides=6, count=2)
        total = sum(results)
        total_rolls += 1

        # Красивый вывод
        print(f"  Выпало: {results[0]} и {results[1]}  →  Сумма: {total}")

        # Небольшая пасхалка
        if results[0] == 6 and results[1] == 6:
            print("  🔥 Двойная шестёрка! Удача на твоей стороне!")
        elif results[0] == 1 and results[1] == 1:
            print("  💀 Две единицы... Змеиные глаза. Не повезло.")


if __name__ == "__main__":
    main()
