import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Seleccionar un pivote aleatorio
        pivot_idx = random.randint(0, len(arr) - 1)
        pivote = arr[pivot_idx]
        # Crear una nueva lista excluyendo el pivote
        resto = arr[:pivot_idx] + arr[pivot_idx + 1:]
        menores = [x for x in resto if x <= pivote]
        mayores = [x for x in resto if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Caso 1: Arreglos aleatorios
arreglo_aleatorio = [9, 3, 7, 6, 2, 8, 5]
print(f"Arreglo aleatorio ordenado: {quicksort(arreglo_aleatorio)}")

# Caso 2: Arreglos ya ordenados
arreglo_ordenado = [1, -3, 85, 4, 1023]
print(f"Arreglo ya ordenado: {quicksort(arreglo_ordenado)}")

# Caso 3: Arreglos en orden inverso
arreglo_inverso = [5, 4, 3, 2, 1]
print(f"Arreglo en orden inverso: {quicksort(arreglo_inverso)}")




