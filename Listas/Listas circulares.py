from graphviz import Digraph

class Node:
    def __init__(self, data):
        self.data = data # Dato o valor que almacena el nodo
        self.next = None # Referencia al siguiente nodo

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def traverse (self):
        if self.head is None:
            print("La lista esta vacia")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current.next == self.head:
                break
        print("(Regresa al inicio)")

def visualize_circular_linked_list(cll):
    """
    Dibuja la lista circular simplemente enlazada usando Graphviz.
    Cada nodo es un óvalo con el 'data'.
    Se dibuja una flecha desde un nodo hacia el siguiente, y desde el último nodo al primero.
    """
    dot = Digraph(comment="Circular Linked List")
    dot.attr(rankdir="LR")  # Orienta el grafo de izquierda a derecha

    if cll.head is None:
        dot.node("Empty", label="Lista vacía")
        return dot

    current = cll.head
    index = 0  # Para dar nombre único a cada nodo
    while True:
        node_name = f"Node{index}"
        dot.node(node_name, label=str(current.data), shape="ellipse")
        if current.next != cll.head:
            dot.edge(node_name, f"Node{index + 1}", label="next")
        else:
            dot.edge(node_name, f"Node{index}", label="next")
            break
        current = current.next
        index += 1

    return dot

# Crear la lista circular simplemente enlazada y visualizarla
lista = CircularLinkedList()
lista.insert_at_end("Tarea1")
lista.insert_at_end("Tarea2")
lista.insert_at_end("Tarea3")
lista.insert_at_end("Tarea4")
lista.insert_at_end("Tarea5")

dot_obj = visualize_circular_linked_list(lista)
dot_obj # SOLO FUNCIONA EN COLAB