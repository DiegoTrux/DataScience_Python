def leaky_relu(x):
    if x > 0:
        return x
    else:
        return 0.01 * x
