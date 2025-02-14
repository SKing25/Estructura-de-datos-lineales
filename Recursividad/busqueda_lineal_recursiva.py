def busqueda_lineal_recursiva(lista, objetivo, indice=0):
    # caso base 1: indice se sale de los limites de la lista
    if indice == len(lista):
        return -1 # no se encontro el elemento

    # caso base 2: elemento encontrado
    if lista[indice] == objetivo:
        return indice

    # llamada recursiva: incrementar indice
    return busqueda_lineal_recursiva(lista, objetivo, indice+1)

mi_lista = [3, 5, 2, 9, 10]
indice_encontrado = busqueda_lineal_recursiva(mi_lista, 9)
print(indice_encontrado)