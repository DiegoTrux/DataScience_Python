import numpy as np

def coseno(a, b):
    # Calcula el producto interno entre a y b
    producto_interno = np.dot(a, b)

    # Calcula las normas L2 de los vectores a y b
    norma_a = np.linalg.norm(a)
    norma_b = np.linalg.norm(b)

    # Calcula la similaridad del coseno
    similaridad_coseno = producto_interno / (norma_a * norma_b)

    return similaridad_coseno