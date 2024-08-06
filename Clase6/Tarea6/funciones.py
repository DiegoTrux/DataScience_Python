import pandas as pd
import string

def generar_dataframe(M, N):
    # Verificar que N sea menor que 300
    if N >= 300:
        raise ValueError("N debe ser menor que 300.")

    # Generar nombres de columnas
    letras = string.ascii_lowercase
    nombres_columnas = []
    for i in range(N):
        if i < 26:
            nombres_columnas.append(letras[i])
        else:
            letras_base = letras[i % 26]
            letras_extras = letras[i // 26 - 1]
            nombres_columnas.append(letras_extras + letras_base)

    # Generar matriz de unos
    matriz_unos = [[1]*N for _ in range(M)]

    # Crear DataFrame
    df = pd.DataFrame(matriz_unos, columns=nombres_columnas)

    return df