def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de n recursivamente.
    :param n: Numero entero no negativo
    :return: Factorial de n
    """
    if n <= 1:
        return 1
    return n * factorial_recursivo(n-1)

def factorial_iterativo(n: int) -> int:
    """
    Calcula el factorial de n iterativamente.
    :param n: Numero entero no negativo
    :return: Factorial de n
    """
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
