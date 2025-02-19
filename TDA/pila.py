class Pila:
    def __init__(self):
        self.data = []

    def push(self, element):
        """Agrega un elemento a la pila"""
        self.data.append(element)

    def pop(self):
        """Elimina y devuelve el ultimo elemento"""
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("La pila esta vacia")

    def peek(self):
        """Devuelve el ultimo elemento sin eliminarlo"""
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("La pila esta vacia")

    def is_empty(self):
        """Comprueba si la pila esta vacia"""
        return len(self.data) == 0

mi_pila = Pila()

#insertar elementos
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(3)
print("Pila despues de insertar elementos: ", mi_pila.data)

#consultar el ultimo elemento
print("Ultimo elemento: ", mi_pila.peek())

#elminar elementos
print("Elemento elminado: ", mi_pila.pop())
print("Pila despuesde eliminar elemento: ", mi_pila.data)

#verificar si esta vacia
print("La pila esta vacia?: ", mi_pila.is_empty())