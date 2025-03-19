class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def eliminar_cabeza(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        if self.cabeza.siguiente == self.cabeza:  # Solo un nodo
            self.cabeza = None
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente

    def eliminar_cola(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
        else:
            temp = self.cabeza
            while temp.siguiente.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = self.cabeza

    def recorrer(self):
        if self.cabeza is None:
            print("Lista vacía.")
            return
        temp = self.cabeza
        while True:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
            if temp == self.cabeza:
                break
        print("(Regresa al inicio)")

# Ejemplo de uso
lista = ListaCircular()
lista.insertar("Nodo 1")
lista.insertar("Nodo 2")
lista.insertar("Nodo 3")
lista.insertar("Nodo 4")

print("Lista circular:")
lista.recorrer()

print("\nEliminando la cabeza...")
lista.eliminar_cabeza()
lista.recorrer()

print("\nEliminando la cola...")
lista.eliminar_cola()
lista.recorrer()