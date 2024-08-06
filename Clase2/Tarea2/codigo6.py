import math

def f(x):
    return math.cos(x) + x

def calcular_area_trapecios(a, b, delta):
    area_total = 0.0

    x = a

    while x < b:
        area_trapecio = delta * (f(x) + f(x + delta)) / 2

        area_total += area_trapecio

        x += delta

    return area_total

a = int(input())
b = int(input())

delta = 0.001

area = "{:.2f}".format(calcular_area_trapecios(a, b, delta))

print(area)