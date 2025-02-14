from collections import deque

def contar_elementos_cola(cola):
    # caso base: si la cola esta vacia
    if not cola:
        return 0

    # tomamos (desencolamos) el frente de la cola
    temp = cola.popleft()
    cantidad = 1 + contar_elementos_cola(cola)

    # lo volvemos a encolar
    cola.append(temp)

    return cantidad

# ejemplo
mi_cola = deque([10, 20, 30, 40, 50])
print(contar_elementos_cola(mi_cola)) # 5
print(mi_cola) # deque([10, 20, 30, 40, 50]), la cola se mantiene igual