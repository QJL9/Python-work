import math

ax=eval(input("请输入第一个点的横坐标："))
ay=eval(input("请输入第一个点的纵坐标："))
bx=eval(input("请输入第二个点的横坐标："))
by=eval(input("请输入第二个点的纵坐标："))

print("distance=","{:.2f}".format(math.sqrt((ax-bx)**2+(ay-by)**2)))