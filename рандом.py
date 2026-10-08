import random

secret = random.randint(1, 10)
guess = int(input("Угадай число от 1 до 10: "))

if guess == secret:
    print("Угадал!")
else:
    print(f"Не угадал, было {secret}")