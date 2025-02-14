def fibonacci(n):
    """
    retorna el n-esimo numero de fibonacci de forma recursiva
    F(0) = 0, F(1)  =1,
    F(n) = F(n-1) + (n-2) para n >= 2
    """
    #caso base 1
    if n == 0:
        return 0

    #caso base 2
    if n == 1:
        return 1

    #llamada recursiva
    return fibonacci(n-1) + fibonacci(n-2)

#ejemplo de uso
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")