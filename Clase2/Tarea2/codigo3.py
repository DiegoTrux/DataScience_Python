i = int(input())

def calcular_termino_s(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return calcular_termino_s(i-1) + calcular_termino_s(i-2)

resultado = calcular_termino_s(i-1)
print(resultado)
