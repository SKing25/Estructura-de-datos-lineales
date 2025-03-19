from graphviz import Digraph


class Node:
    def __init__(self, data):
        self.data = data  # Dato o valor que almacena el nodo
        self.next = None  # Referencia al siguiente nodo


class SingleLinkedList:
    def __init__(self):
        self.head = None  # Cabeza de la lista

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_position(self, pos, data):
        """ Inserta un nuevo nodo en la posición dada (0-based index). """
        if pos < 0:
            print("La posición no es válida.")
            return

        new_node = Node(data)

        if pos == 0:  # Insertar al inicio
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current is not None and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("La posición excede el tamaño de la lista.")
            return

        new_node.next = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def length(self):
        """ Retorna el número de nodos en la lista. """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def traverse(self):
        """ Recorre la lista e imprime sus elementos. """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def visualize_singly_linked_list(sll):
    """Dibuja la lista simplemente enlazada usando Graphviz."""
    dot = Digraph(comment="Singly Linked List")
    dot.attr(rankdir="LR")  # Orientación de izquierda a derecha

    if sll.head is None:
        dot.node("Empty", label="Lista vacía")
        return dot

    current = sll.head
    index = 0  # Para nombres únicos
    while current is not None:
        node_name = f"Node{index}"
        dot.node(node_name, label=str(current.data), shape="ellipse")
        if current.next is not None:
            dot.edge(node_name, f"Node{index + 1}", label="next")
        current = current.next
        index += 1

    return dot


# Pruebas de los métodos implementados
lista = SingleLinkedList()
lista.insert_at_end("Tarea1")
lista.insert_at_end("Tarea2")
lista.insert_at_end("Tarea3")

# Insertando en una posición específica
lista.insert_at_position(1, "NuevaTarea")

# Mostrando la lista
lista.traverse()

# Obteniendo la longitud
print("Longitud de la lista:", lista.length())

# Visualización (en Colab)
dot_obj = visualize_singly_linked_list(lista)
dot_obj
