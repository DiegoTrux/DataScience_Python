import pandas as pd

# URL del conjunto de datos
filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

def leer_wine_alcohol_mayor_13(filename):
    # Definir los nombres de las columnas
    columnas = ['Wine_class', 'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_ash', 'Magnesium',
                'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins',
                'Color_intensity', 'Hue', 'OD280_OD315_diluted_wines', 'Proline']

    # Leer el conjunto de datos
    df = pd.read_csv(filename, header=None, names=columnas)

    # Filtrar las filas donde Alcohol es mayor que 13
    df_filtrado = df[df['Alcohol'] > 13]

    return df_filtrado