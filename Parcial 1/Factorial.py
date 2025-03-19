def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de n recursivamente.
    :param n: Número entero no negativo.
    :return: Factorial de n.
    """
    # -------------------------------------------
    # Paso 1: Caso base (0! = 1 y 1! = 1)
    # -------------------------------------------
    if n <= 1:
        return 1

    # -------------------------------------------
    # Paso 2: Llamada recursiva (n! = n * (n-1)!)
    # -------------------------------------------
    return n * factorial_recursivo(n - 1)

# -------------------------------------------
# Ejemplo de ejecución con n=5:
# -------------------------------------------
# Llamada inicial: factorial_recursivo(5)
#   → Calcula 5 * factorial_recursivo(4)
#
# factorial_recursivo(4):
#   → Calcula 4 * factorial_recursivo(3)
#
# factorial_recursivo(3):
#   → Calcula 3 * factorial_recursivo(2)
#
# factorial_recursivo(2):
#   → Calcula 2 * factorial_recursivo(1)
#
# factorial_recursivo(1):
#   → Retorna 1 (caso base)
#
# Regresos:
# factorial_recursivo(2) → 2 * 1 = 2
# factorial_recursivo(3) → 3 * 2 = 6
# factorial_recursivo(4) → 4 * 6 = 24
# factorial_recursivo(5) → 5 * 24 = 120
#
# Resultado final: 120
# -------------------------------------------

# Ejemplo de uso
numero = 5
print(f"Factorial de {numero}: {factorial_recursivo(numero)}")