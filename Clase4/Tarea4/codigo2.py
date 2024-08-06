import numpy as np

def neurona_artificial(x, w, b):
    pre_activacion = np.dot(x, w) + b

    return pre_activacion