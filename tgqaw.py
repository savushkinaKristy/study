import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль заданной длины."""
    # Наборы символов
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    # Объединяем все символы
    all_chars = lowercase + uppercase + digits + symbols

    # Гарантируем, что в пароле будет хотя бы по одному символу каждого типа
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Добавляем остальные символы до нужной длины
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Перемешиваем, чтобы символы не шли по порядку
    random.shuffle(password)

    return "".join(password)

def check_strength(password):
    """Оценивает надежность пароля."""
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1

    if score == 5:
        return "Очень надежный"
    elif score >= 3:
        return "Средний"
    else:
        return "Слабый"

def main():
    print("=== Генератор паролей ===")
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
    except ValueError:
        print("Некорректный ввод. Использую длину 12.")
        length = 12

    if length < 4:
        print("Минимальная длина — 4 символа. Использую 4.")
        length = 4

    password = generate_password(length)
    print(f"\nВаш пароль: {password}")
    print(f"Надежность: {check_strength(password)}")

    # Предложение сгенерировать еще один
    while True:
        again = input("\nСгенерировать еще один? (да/нет): ").strip().lower()
        if again in ("да", "д", "yes", "y"):
            password = generate_password(length)
            print(f"\nНовый пароль: {password}")
            print(f"Надежность: {check_strength(password)}")
        else:
            print("Готово! Не забудьте сохранить пароль в надежном месте.")
            break

if __name__ == "__main__":
    main()
