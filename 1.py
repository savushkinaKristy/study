import random

def guess_the_number():
    # Компьютер загадывает число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1

            if guess < secret_number:
                print("Больше! Попробуй ещё.")
            elif guess > secret_number:
                print("Меньше! Попробуй ещё.")
            else:
                print(f"🎉 Угадал! Это было число {secret_number}. Ты справился за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введи целое число.")

# Запуск игры
if __name__ == "__main__":
    guess_the_number()