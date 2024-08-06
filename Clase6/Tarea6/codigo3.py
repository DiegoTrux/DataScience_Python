import pandas as pd

def lectura_annealing(filename):
    # Definir los nombres de las columnas
    columnas = ['family', 'product-type', 'steel', 'carbon', 'hardness', 'temper_rolling',
                'condition', 'formability', 'strength', 'non-ageing', 'surface-finish',
                'surface-quality', 'enamelability', 'bc', 'bf', 'bt', 'bw_me', 'bl', 'm',
                'chrom', 'phos', 'cbond', 'marvi', 'exptl', 'ferro', 'corr',
                'blue_bright_varn_clean', 'lustre', 'jurofm', 's', 'p', 'shape',
                'thick', 'width', 'len', 'oil', 'bore', 'packing', 'class_value']

    # Leer el conjunto de datos con valores '?' interpretados como NaN
    df = pd.read_csv(filename, header=None, names=columnas, na_values='?')

    return df