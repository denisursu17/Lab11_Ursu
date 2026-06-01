import math

def circle_info(r):
    area = round(math.pi * r ** 2, 2)
    length = round(2 * math.pi * r, 2)
    return (area, length)

r = float(input("Радіус: "))
print(circle_info(r))
