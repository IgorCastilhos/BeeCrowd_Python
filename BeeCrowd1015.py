import math

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

# p1(x1,y1)
# p2(x2,y2)

distancia = math.sqrt(((x2 - x1)**2) + (y2 - y1)**2)

print("%.4f"%distancia)