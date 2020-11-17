i=0
for i in range(1,3+1):
    print(i,"号")
    a=eval(input("年龄:"))
    b=eval(input("经验:"))
    c=input("专业:")
    if (a<25 and c=="计算机"):
        print("获得面试机会")
    elif c=="电子" and b>4:
        print("获得面试机会")
    elif c=="通信":
        print("获得面试机会")
    else:
        print("抱歉，您不符合面试要求")

