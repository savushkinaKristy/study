import random
import string
def generate_password(length, use_lower, use_upper, use_number, use_special):
    """
    Генерирует случайный пароль заданной длины на основе выбранных настроек.

    Args:
        length (int): Длина пароля.
        use_lower (bool): Включать ли строчные буквы.
        use_upper (bool): Включать ли заглавные буквы.
        use_number (bool): Включать ли цифры.
        use_special (bool): Включать ли специальные символы (пунктуацию).

    Returns:
        str: Сгенерированный пароль.

    Example:
        >>> generate_password(5, True, False, True, False)
        'a3b1c'
        >>> generate_password(3, False, False, True, False)
        '742'
    """

    content = ""
    if use_lower == True:
        content += "abcdefghijklmnopqrstuvwxyz" # наличие нижнего регисра
    if use_upper == True:
        content += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # верхнего регистра
    if use_number==True:
        content += "0123456789" # цифр
    if use_special==True:
        content += string.punctuation # спец символов

    password=[]
    for _ in range(length):
        result = random.choice(content)
        password.append(result)
    return "".join(password)

print("-" * 50)
print("\033[36m🔐ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ🔑\033[0m")
print("-" * 50)
length = int(input("Введите желаемую длину пароля 📏: "))
print()
answer = input("Использовать нижний регистр? (✅/❌) ")
if answer in ["да", "yes", "1"]:
    use_lower = True
else:
    use_lower = False
print()
answer = input("Использовать верхний регистр? (✅/❌) ")
if answer in ["да", "yes", "1"]:
    use_upper = True
else:
    use_upper = False
print()
answer = input("Использовать цифры? (✅/❌) ")
if answer in ["да", "yes", "1"]:
    use_number = True
else:
    use_number = False
print()
answer = input("Использовать спец символы? (✅/❌) ")
if answer in ["да", "yes", "1"]:
    use_special = True
else:
    use_special = False
password = generate_password(length, use_lower, use_upper, use_number, use_special)
print("-" * 50)
print(f"\033[31m🎉🎉🎉Ваш пароль готов!🎉🎉🎉\033[0m")
print("-" * 50)
print(f"{password}")



