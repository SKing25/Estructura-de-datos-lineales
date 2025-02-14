def imprimir_lista(lista, indice=0):
    #caso base: si elindice se sale de la longitud de la lista
    if indice == len(lista):
        return

    #procesar (imprimir) el elemento en la posicion 'indice'
    print(lista[indice])

    #llamada recursiva incrementando el indice
    imprimir_lista(lista, indice+1)

#ejemplo
mi_lista = [10, 20, 30, 40, 50]
imprimir_lista(mi_lista)