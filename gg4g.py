for A in range(1, 100):
    flag = True
    for x in range(1,1000):
        if (((x % A != 0) or (x % 6 != 0)) <= (x % 8 != 0)) == 0:
            flag = False
    if flag == True:
        print(A)
