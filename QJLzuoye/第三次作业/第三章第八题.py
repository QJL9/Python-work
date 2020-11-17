import random
a=random.randrange(1,100)
b=random.randrange(1,100)
print(a,b)
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print("最大公约数为：",i)
        break
for j in range(max(a,b),a*b+1):
    if j%a==0 and j%b==0:
        print("最小公倍数为：",j)
        break
