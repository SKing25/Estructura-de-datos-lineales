def mergeSort(arr):
    if len(arr) <= 1:  # Si la longitud del arreglo es 1 o menor, ya está ordenado
        return arr  # Retornar el arreglo tal cual, ya que no necesita ordenarse
    mid = len(arr) // 2  # Calcular el punto medio del arreglo para dividirlo en dos mitades
    left = mergeSort(arr[:mid])  # Ordenar recursivamente la mitad izquierda del arreglo
    right = mergeSort(arr[mid:len(arr)])  # Ordenar recursivamente la mitad derecha del arreglo
    return merge(left, right)  # Combinar las dos mitades ordenadas y retornar el resultado


def merge(left, right):
    result = []  # Inicializar un arreglo vacío para almacenar el resultado combinado
    i = j = 0  # Inicializar índices para recorrer las mitades de la izquierda (i) y de la derecha (j)
    while i < len(left) and j < len(right):  # Mientras haya elementos en ambas mitades
        if left[i] <= right[j]:  # Si el elemento de la mitad izquierda es menor o igual
            result.append(left[i])  # Agregar el elemento de la mitad izquierda al resultado
            i += 1  # Avanzar el índice de la mitad izquierda
        else:  # Si el elemento de la mitad derecha es menor
            result.append(right[j])  # Agregar el elemento de la mitad derecha al resultado
            j += 1  # Avanzar el índice de la mitad derecha

    # Si quedan elementos en la mitad izquierda, agregarlos al resultado
    while i < len(left):
        result.append(left[i])
        i += 1

    # Si quedan elementos en la mitad derecha, agregarlos al resultado
    while j < len(right):
        result.append(right[j])
        j += 1

    return result  # Retornar el arreglo combinado y ordenado

# --------------- CASOS DE PRUEBA ---------------

# Caso 1: Arreglo desordenado
# Entrada: [38, 27, 43, 3, 9, 82, 10]
# División: [38,27,43] | [3,9,82,10] → ... → subarreglos de 1 elemento
# Fusión: [3,9,10,27,38,43,82]
# Salida Esperada: [3, 9, 10, 27, 38, 43, 82]

# Caso 2: Arreglo ya ordenado
# Entrada: [1, 2, 3, 4, 5]
# Salida Esperada: [1, 2, 3, 4, 5]

# Caso 3: Arreglo en orden inverso
# Entrada: [5, 4, 3, 2, 1]
# Salida Esperada: [1, 2, 3, 4, 5]

# Caso 4: Elementos duplicados
# Entrada: [5, 2, 5, 3, 1]
# Salida Esperada: [1, 2, 3, 5, 5]

# Caso 5: Arreglo vacío y un solo elemento
# Entrada 1: []
# Salida Esperada 1: []
# Entrada 2: [7]
# Salida Esperada 2: [7]

# Caso 6: Números negativos
# Entrada: [-3, 0, 4, -1, 2]
# Salida Esperada: [-3, -1, 0, 2, 4]

# --------------- EJECUCIÓN ---------------

# Lista desordenada
arr = [38, 27, 43, 3, 9, 82, 10]
arr1 = [1, 52, 3, 6, 5]
arr2 = [30, 65, 11, 2, 0]
# Ordenar la lista usando mergeSort
sorted_arr = mergeSort(arr)
sorted_arr1 = mergeSort(arr1)
sorted_arr2 = mergeSort(arr2)

# Imprimir la lista ordenada
print("Lista ordenada:", sorted_arr)
print("Lista ordenada:", sorted_arr1)
print("Lista ordenada:", sorted_arr2)