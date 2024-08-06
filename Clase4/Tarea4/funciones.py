import numpy as np

def angulo(a, b):
    producto_interno = np.dot(a, b)

    norma_a = np.linalg.norm(a)
    norma_b = np.linalg.norm(b)

    coseno_angulo = producto_interno / (norma_a * norma_b)

    coseno_angulo = np.clip(coseno_angulo, -1, 1)

    angulo_radianes = np.arccos(coseno_angulo)

    return angulo_radianes