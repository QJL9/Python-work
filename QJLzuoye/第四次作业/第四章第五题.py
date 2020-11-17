import random
l=[]
for i in range(0,20):
    l.append(random.randrange(1000,5000+1))
print(l)
for i in l:
    if i %2*3*5*7!=0:
        print(i)