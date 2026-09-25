from collections import Counter
stroka=input().lower().replace(" ","")#не считая регистра
a=Counter(stroka) #считает символы все
top=a.most_common(3) #нахолит топ 3 самых частых
print(top)

