number=int(input())
if number%2==0:
    print("число четное")
else:
    print("число нечетное")
if number>0:
    print("число положительное")
elif number<0:
    print("Число отрицательное")
else:
    print("число рано 0")
if 10<=number<=50:
    print("число пренадлежит диапозону [10, 50]")
else:
    print("число не пренадлежит диапозону [10, 50]")
