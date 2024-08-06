def cadena_binaria(texto):
    # Convierte la cadena a un conjunto para obtener los caracteres únicos
    caracteres_unicos = set(texto)
    
    # Verifica si la cadena es binaria (contiene uno o dos símbolos)
    if len(caracteres_unicos) <= 2:
        return True
    else:
        return False