import pandas as pd

def leer_red_wine_quality_mayor_3(filename):
    # Leer el conjunto de datos con el separador correcto
    df = pd.read_csv(filename, sep=';')

    # Filtrar las filas donde quality es mayor que 3
    df_filtrado = df[df['quality'] > 3]

    return df_filtrado