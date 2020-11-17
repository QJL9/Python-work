import math
for i in range(0,91,5):
    print(i)
    print("sin=","{:.2f}".format(math.sin(i/360*2*math.pi)))
    print("cos=","{:.2f}".format(math.cos(i/360*2*math.pi)))
