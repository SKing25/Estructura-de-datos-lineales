def potencia(a,b):
    """calcula a^b usando recursion"""
    # caso base
    if b == 0:
        return 1

    # llamada recursiva
    return a * potencia(a,b-1)

print(potencia(3,20))