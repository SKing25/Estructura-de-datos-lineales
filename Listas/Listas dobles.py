from graphviz import Digraph


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, key, data):
        current = self.head
        while current is not None and current.data != key:
            current = current.next

        if current is None:
            print(f"El nodo con valor {key} no se encontró.")
            return

        new_node = DoublyNode(data)
        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node
        else:
            self.tail = new_node  # Si se inserta al final, actualizar tail

        current.next = new_node

    def remove(self, key):
        if self.head is None:
            print("La lista está vacía")
            return

        current = self.head
        while current is not None and current.data != key:
            current = current.next

        if current is None:
            print(f"El elemento {key} no está en la lista")
            return

        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif current == self.tail:
            self.tail = current.prev
            if self.tail:
                self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def traverse_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def visualize(self):
        dot = Digraph(comment="Doubly Linked List")
        dot.attr(rankdir="LR")

        if self.head is None:
            dot.node("Empty", label="Lista vacía")
            return dot

        current = self.head
        index = 0
        while current is not None:
            node_name = f"Node{index}"
            dot.node(node_name, label=str(current.data), shape="ellipse")
            if current.next is not None:
                dot.edge(node_name, f"Node{index + 1}", label="next")
                dot.edge(f"Node{index + 1}", node_name, label="prev")
            current = current.next
            index += 1

        return dot


# Pruebas con la lista
lista = DoublyLinkedList()
lista.insert_at_end("Tarea1")
lista.insert_at_end("Tarea2")
lista.insert_at_end("Tarea3")
lista.traverse_forward()
lista.traverse_backward()

# Insertar después de un nodo específico
lista.insert_after("Tarea2", "Tarea2.5")
lista.traverse_forward()

# Eliminar primer y último elemento
lista.remove("Tarea1")
lista.remove("Tarea3")
lista.traverse_forward()
