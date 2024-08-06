import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distancia_maxima = float(input())

conductores = []
while True:
    nombre = str(input())
    
    if nombre.upper() == "FIN":
        break
    
    x = float(input())
    y = float(input())
    
    conductores.append((nombre, x, y))

distancia_minima = float('inf')
conductor_mas_cercano = None

for conductor in conductores:
    nombre, x, y = conductor
    distancia = calcular_distancia(0, 0, x, y)
    
    if distancia < distancia_minima:
        distancia_minima = distancia
        conductor_mas_cercano = nombre

if distancia_minima > distancia_maxima:
    print("muy lejos")
else:
    print(conductor_mas_cercano)
