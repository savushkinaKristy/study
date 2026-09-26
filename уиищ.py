#5
def f(N):
    n=bin(N)[2:]
    if N%5==0: n=n+"101"
    else: n=n+"1"
    if int(n)%7==0: n=n+"111"
    else: n=n+"1"
    return int(n,2)
print(max(N for N in range(1,10000000) if f(N)<1855663))
#6
from turtle import *
tracer(0)
left(90)
k=17
right(30)
for _ in range(3):
    right(150)
    fd(6*k)
    right(30)
    fd(12 * k)
pu()
for x in range(-100,100):
    for y in range(-100,100):
        goto(k*x,k*y)
        dot(7)
done()
#8
from itertools import permutations
k=0
for x in set(permutations("АНАСТАСИЯ",r=9)):
    x="".join(x)
    x1=x
    for c in "АИЯ": x1=x1.replace(c,"А")
    for c in "НСТ": x1=x1.replace(c,"Н")
    if "ААА" not in x1 or "ННН" not in x1:
        k+=1
print(k)
#9
k=0
for line in open("9.txt"):
    a=[int(x) for x in line.split()]
    pp=[x for x in a if a.count(x)>1]
    a.sort()
    if ((len(pp)>=2)+(a[0]==(a[2]-a[1])==(a[4]-a[3])==(a[5]-a[4])))>=1:
        k+=1
print(k)
#13
from ipaddress import ip_network
k=0
net=ip_network("192.168.32.160/255.255.255.240",0)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip.count("1")%2==0:
        k+=1
print(k)
#14
from string import printable
for x in printable[:15]:
    x1=int(f"6{x}839",15)
    x2=int(f"5793{x}{x}5",15)
    x3=int(f"53129{x}",15)
    x4=int(f"14{x}677935",15)
    if (x1+x2+x3+x4)%14==0:
        print((x1+x2+x3+x4)//14)
#15
def t(n,m,k):
    if n>(k+m): return n>(k+m)
    if k>(n+m): return k>(n+m)
    if m>(k+n): return m>(k+n)
def m(a,b):
    if a>b: return a
    if a<=b: return b
def f(x,A):
    return (t(A,5,x))<=(((m(x,11))<=19)==(not(t(23,13,x))))
print(max(A for A in range(1,200) if all(f(x,A) for x in range(1,600))))
#16
def f(n):
    if n==0: return 0
    if n>0 and n%2==0: return f(n/2)-1
    if n>0 and n%2!=0: return 1+f(n-1)
print(len([n for n in range(0,1000) if f(n)==0]))
#17
a=[int(x) for x in open("9.txt")]
s=[]
def f(x):
    return x<0
def p(x):
    return x>0
for i in range(len(a)-2):
    x1,x2,x3=a[i],a[i+1],a[i+2]
    if abs(f(x1)+f(x2)+f(x3))<=(p(x1)+p(x2)+p(x3)):
        m=(x1*x2*x3)
        if str(m)[-1]==str(max(a))[-1]:
            if f(x1) not in a and f(x2) not in a and f(x3) not in a: (f(x1)+f(x2)+f(x3))==0
            if p(x1) not in a and p(x2) not in a and p(x3) not in a: (p(x1)+p(x2)+p(x3))==0
            s.append(abs(x1)*abs(x2)*(abs(x3)))
print(len(s),max(s))
#19-21
def f(s,m):
    if s>=59: return m%2==0
    if m==0: return 0
    h=[f(s+1,m-1),f(s+3,m-1),f(s*4,m-1)]
    return any(h) if m%2!=0 else all(h)
print([s for s in range(1,59) if not f(s,1) and f(s,3)])
print([s for s in range(1,59) if not f(s,2) and f(s,4)])
#23
def f(x,end):
    if x>end: return 0
    if x==end: return 1
    return f(x+4,end)+f(x*2,end)
print(f(13,42))
#24
s=open("9.txt").readline()
m=0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if "PP" in c and "PPP" in c: break
        if "PP" not in c and "PPP" not in c: m=len(c)
print(m)
#25

