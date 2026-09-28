def p(x):
    return x>1 and all(x%d!=0 for d in range(2,int(x**0.5)+1))
def f(x):
    D=[]
    for d in range(1,int(x**0.5)+1):
        if x%d==0:
            if p(d) and p(x//d):
                if str(d).count("5")==1 and str(x//d).count("5")==1:
                    D.append(d)
                    D.append(x//d)
    return 0
x=1_324_728
count=0
while count<5:
    Dx=f(x)
    if len(Dx) == 2:
        count+=1
        print(x,max(Dx))
    x+=1
