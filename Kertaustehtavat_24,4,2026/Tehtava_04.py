import math

def create_point(x, y):
    return (x, y)

x1 = float(input("Anna ensimmäisen pisteen x-arvo: "))
y1 = float(input("Anna ensimmäisen pisteen y-arvo: "))
p1 = create_point(x1, y1)

x2 = float(input("Anna toisen pisteen x-arvo: "))
y2 = float(input("Anna toisen pisteen y-arvo: "))
p2 = create_point(x2, y2)

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

d = distance(p1, p2)
print("Pisteiden välinen etäisyys:", d)
