from graphviz import Digraph

class Node:
    def __init__(self, data):
        self.data = data # Dato o valor que almacena el nodo
        self.next = None # Referencia al siguiente nodo

class SingleLinkedList:
    def __init__(self):
        self.head = None # Cabeza de la lista

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

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def visualize_singly_linked_list(sll):
    """Dibuja la lista simplemente enlazada usando Graphviz.
    Cada nodo es un óvalo con el 'data'.
    Se dibuja una flecha desde un nodo hacia el siguiente.
    """
    dot = Digraph(comment="Singly Linked List")
    dot.attr(rankdir="LR") # orienta el grafo de izquierda a derecha

    if sll.head is None:
        dot.node("Empty", label="Lista vacía")
        return dot

    current = sll.head
    index = 0 # Para dar nombre único a cada nodo
    while current is not None:
        node_name = f"Node{index}"
        dot.node(node_name, label=str(current.data), shape="ellipse")
        if current.next is not None:
            dot.edge(node_name, f"Node{index+1}", label="next")
        current = current.next
        index += 1

    return dot

# Crear la lista enlazada y visualizarla
lista = SingleLinkedList()
lista.insert_at_end("Tarea1")
lista.insert_at_end("Tarea2")
lista.insert_at_end("Tarea3")

dot_obj = visualize_singly_linked_list(lista)
dot_obj # SOLO FUNCIONA EN COLAB
