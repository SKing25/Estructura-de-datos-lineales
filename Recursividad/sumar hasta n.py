def sumar_hasta_n(n: object) -> object:
    # caso base
    if n == 0:
        return 0

    # llamada recursiva
    return n + sumar_hasta_n(n-1)

# ejemplo
print(sumar_hasta_n(50))