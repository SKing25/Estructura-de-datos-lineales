def contar_elementos_pila(pila):
    #caso base: si la pila esta vacia
    if not pila:
        return 0

    #desapilamos un elemento temporalmente
    temp = pila.pop()
    cantidad = 1 + contar_elementos_pila(pila)

    #lo volvemos a apilar para no perder la estructura original
    pila.append(temp)

    return cantidad

#ejemplo
mi_pila = [1, 2, 3, 4, 5] #usamos lista con pila
print(contar_elementos_pila(mi_pila)) #5
# la pila sigue intacta al final de la funcion
print(mi_pila) 