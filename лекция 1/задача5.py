numbers=list(range(2,31))
prost=[]
while numbers:
    first=numbers[0]
    prost.append(first)
    for i in numbers.copy():
        if i%first==0:
            numbers.remove(i)
print(prost)
