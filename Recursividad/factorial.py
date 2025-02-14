def factorial(n):
    # caso base
    if n == 0:
        return 1

    # llamada recursiva
    return n * factorial(n - 1)

# ejemplo de uso
print(factorial(5)) #120