from itertools import*
def f(x):
    P=1<=x<=98
    Q=25<=x<=42
    A=a1<=x<=a2
    return Q<=(((not P)and Q)<= A)
Ox=[i/4 for i in range(0*4,100*4)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        m.append(a2-a1)
print(round(min(m)))
        
