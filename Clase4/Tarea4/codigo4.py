import numpy as np

def chebyshev(a, b):
    # Calcula la distancia de Chebyshev
    diferencia_absoluta = np.abs(a - b)
    distancia_chebyshev = np.max(diferencia_absoluta)

    return distancia_chebyshev