def calculadora(expresion):
    # Divide la expresión en número, operador y número
    elementos = expresion.split()
    
    # Extrae los operandos y el operador
    operando1 = float(elementos[0])
    operador = elementos[1]
    operando2 = float(elementos[2])
    
    # Realiza la operación correspondiente
    if operador == '+':
        resultado = operando1 + operando2
    elif operador == '-':
        resultado = operando1 - operando2
    elif operador == 'x':
        resultado = operando1 * operando2
    else:
        # Manejo de operador no válido
        raise ValueError("Operador no válido. Use '+', '-', o 'x'.")
    
    return resultado