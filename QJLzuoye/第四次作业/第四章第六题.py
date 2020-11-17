l=[['王平','男',1,1,0,0],['李丽','女',0,1,0,1],['陈小梅','女',0,0,1,0],['孙洪涛','男',0,1,1,1,],['方亮','男',1,0,1,0]]
j=0
for i in l:
    if i[2]+i[3]+i[4]+i[5]>=:
        j+=1
print(j)

ll=["100m","3000m","跳远","跳高"]
for i in l:
    if i[1]=='女':
        print("{}报名了：".format(i[0]),end="")
        for k in range(2,5+1):
            if i[k]==1:
                print(ll[k-2] ,' ',end="")
        print()

for i in l:
    if i[2]==1:
        print(i[0],i[1])

    
