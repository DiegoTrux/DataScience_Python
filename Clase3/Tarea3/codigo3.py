import math

def distancia_euclidiana(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def punto_mas_cercano(query, coordenadas):
    distancia_minima = float('inf')
    punto_cercano = None

    for punto in coordenadas:
        distancia = distancia_euclidiana(query, punto)
        if distancia < distancia_minima:
            distancia_minima = distancia
            punto_cercano = punto

    return punto_cercano