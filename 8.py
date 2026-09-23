from itertools import*
k=0
for x in product("012345678", repeat=5):
    s="".join(x)
    if s[0] in "2468" and s.count("3")<=1 and s[-1] not in "18":
        k+=1
print(k)
    
    
