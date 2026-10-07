a = float(input("Первое число: "))
b = float(input("Второе число: "))
op = input("Действие (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Неизвестное действие")