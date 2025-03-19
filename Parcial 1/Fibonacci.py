def fibonacci_memo(n, memo=None):
    # Si es la primera llamada, inicializa el diccionario de memoización
    if memo is None:
        memo = {}

    # Si ya hemos calculado F(n), retorna el valor almacenado (memoización)
    if n in memo:
        return memo[n]

    # Casos base: F(0) = 0 y F(1) = 1
    if n < 2:
        memo[n] = n  # Almacena el valor en memo antes de retornar
    else:
        # Paso recursivo con memoización:
        # 1. Calcula F(n-1) reutilizando el mismo diccionario
        # 2. Calcula F(n-2) reutilizando el mismo diccionario
        # 3. Suma ambos resultados y guarda en memo
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    # Retorna el valor almacenado para F(n)
    return memo[n]

# Ejemplo de uso interactivo
pos = 4
print(f"F({pos}) = {fibonacci_memo(pos)}")

# -------------------------------------------
# Ejemplo de ejecución con n=4:
# -------------------------------------------
# Llamada inicial: fibonacci_memo(4)
#   memo = {}
#   → Calcula fibonacci_memo(3, memo) + fibonacci_memo(2, memo)
#
# fibonacci_memo(3, memo):
#   → Calcula fibonacci_memo(2, memo) + fibonacci_memo(1, memo)
#
# fibonacci_memo(2, memo):
#   → Calcula fibonacci_memo(1, memo) + fibonacci_memo(0, memo)
#   → fibonacci_memo(1, memo): memo[1] = 1
#   → fibonacci_memo(0, memo): memo[0] = 0
#   → memo[2] = 1 + 0 = 1
#
# fibonacci_memo(1, memo): ya está en memo → 1
# → memo[3] = 1 + 1 = 2
#
# fibonacci_memo(2, memo): ya está en memo → 1
# → memo[4] = 2 + 1 = 3
#
# Resultado final: 3
# -------------------------------------------