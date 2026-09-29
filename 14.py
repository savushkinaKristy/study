from itertools import*
word="0123456789"
k=0
for j in range(1,11):
    for i in permutations(word,j):
        x="".join(i)
        if (x[-1]=="5" or x[-1]=="0") and x[0]!="0":
            k+=1
print(k)
