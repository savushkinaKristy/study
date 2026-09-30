from turtle import*
tracer(0)
left(90)
k=20
x=3

for _ in range (6):
    fd(x*k)
    right(90)
    fd(7*k)
    


pu()
for x in range (-50,50):
    for y in range (-50,50):
        goto(x*k,y*k)
        dot(5)
done()



    
    
