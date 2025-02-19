class Lista:
    def __init__(self):
        self.data = [] #representacion interna de la lista, puede ser un arreglo

    def append(self, element):
        """Agrega un elemento al final de la lista"""
        self.data.append(element)

    def insert(self, index, element):
        """Inserta un elemento en una posicion especifica"""
        if 0 <= index <= len(self.data):
            self.data.insert(index, element)
        else:
            raise IndexError("Indice fuera de rango")

    def remove(self, index):
        """Elimina un elemento en una posicion especificada"""
        if 0 <= index <= len(self.data):
            return self.data.pop(index)
        else:
            raise IndexError("Indice fuera de rango")

    def get(self, index):
        """Devuelve el elemento en la posicion especificada"""
        if 0 <= index <= len(self.data):
            return self.data[index]
        else:
            raise IndexError("Indice fuera de rango")

    def length(self):
        """Devuelve el numero de elementos en la lista"""
        return len(self.data)

mi_lista = Lista()

#agregar elementos
mi_lista.append(10)
mi_lista.append(20)
mi_lista.append(30)
print("Lista despues de agregar elementos: ", mi_lista.data)

#insertar elementos
mi_lista.insert(1, 15)
print("Lista despues de insertar 15 en la posicion 1: ", mi_lista.data)

#obtener elementos
print("Elemento en la posicion 2: ", mi_lista.get(2))

#elminiar elementos
mi_lista.remove(2)
print("Lista despues de eliminar elementos: ", mi_lista.data)

#longitud de la lista
print("Longitud de la lista: ", mi_lista.length())
