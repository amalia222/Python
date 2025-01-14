import math

x1 = float(input("x1"))
x2 = float(input("x2"))
y1 = float(input("y1"))
y2 = float(input("y2"))
x3 = float(input("x3"))
y3 = float(input("y3"))
a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
P = (a + b + c) / 2
S = math.sqrt(P * (P - a) * (P - b) * (P - c))
print(f"Периметр = {P*2}")
print(f"Площадь = {S}")