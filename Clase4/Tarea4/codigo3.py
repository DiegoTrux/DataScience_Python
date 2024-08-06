import numpy as np

def minkowski(a, b, p):
    # Calcula la distancia de Minkowski
    diferencia_absoluta = np.abs(a - b)
    suma_p = np.sum(np.power(diferencia_absoluta, p))
    distancia_minkowski = np.power(suma_p, 1/p)

    return distancia_minkowski