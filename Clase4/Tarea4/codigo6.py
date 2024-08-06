import numpy as np

def vector_unitario(v):
    # Calcula la norma euclidiana del vector v
    norma_v = np.linalg.norm(v)

    # Verifica que la norma no sea cero para evitar divisiones por cero
    if norma_v == 0:
        raise ValueError("El vector tiene norma cero. No se puede calcular el vector unitario.")

    # Calcula el vector unitario
    u = v / norma_v

    return u