import numpy as np

def promedio_final(NOTAS, pesos):
    if len(NOTAS.shape) != 2 or len(pesos) != NOTAS.shape[1]:
        raise ValueError("Las dimensiones de la matriz de notas y el vector de pesos no son compatibles.")

    pesos_normalizados = np.array(pesos) / np.sum(pesos)

    # Calcula el promedio ponderado para cada estudiante
    promedio_final = np.dot(NOTAS, pesos_normalizados)

    return promedio_final