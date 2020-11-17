import math
def area(r):
    return round(math.pi*r*r,2)
print(area(3.5))
print(area(2.9))
print(round(area(6.2)-area(3.3),2))