from graphviz import Digraph

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None # Referencia al nodo anterior
        self.next = None # Referencia al siguiente nodo

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Suele mantenerse una referencia al final

    def insert_at_begining(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, key):
        if self.head is None:
            print("La lista esta vacia")
            return

        current = self.head
        while current is not None and current.data != key:
            current = current.next

        if current is None:
            print(f"El elemento {key} no esta en la lista")
            return

        # caso 1: el nodo es la cabeza
        if current == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None # lista quedo vacia

        # caso 2: el nodo es la cola
        elif current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # Caso 3: nodo intermedio
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def search(self, target):
        """
        Busca un valor (target) en la lista
        Retorna el nodo que contiene el valor
        o None si no lo encuentra
        """
        current = self.head
        while current is not None:
            if current.data == target:
                return current # retorna el nodo encontrado
            current = current.next
        return None # si no se encontro el valor

    def traverse_forward(self):
        """
        Recorre la lista desde la cabeza hacia la cola,
        imprimiendo los valores de cada nodo
        """
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """
        Recorre la lista desde la cola hacia la cabeza,
        imprimiendo los valores de cada nodo
        """
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

def visualize_doubly_linked_list(dll):
    """
    Dibuja la lista doblemente enlazada usando Graphviz.
    Cada nodo es un óvalo con el 'data'.
    Se dibuja una flecha desde un nodo hacia el siguiente y el anterior.
    """
    dot = Digraph(comment="Doubly Linked List")
    dot.attr(rankdir="LR") # orienta el grafo de izquierda a derecha

    if dll.head is None:
        dot.node("Empty", label="Lista vacía")
        return dot

    current = dll.head
    index = 0 # Para dar nombre único a cada nodo
    while current is not None:
        node_name = f"Node{index}"
        dot.node(node_name, label=str(current.data), shape="ellipse")
        if current.next is not None:
            dot.edge(node_name, f"Node{index + 1}", label="next")
            dot.edge(f"Node{index + 1}", node_name, label="prev")
        current = current.next
        index += 1

    return dot

# Crear la lista doblemente enlazada y visualizarla
lista = DoublyLinkedList()
lista.insert_at_end("Tarea1")
lista.insert_at_end("Tarea2")
lista.insert_at_end("Tarea3")

dot_obj = visualize_doubly_linked_list(lista)
dot_obj # SOLO FUNCIONA EN COLAB