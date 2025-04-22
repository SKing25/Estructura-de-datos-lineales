class Stack:
    """Implementación de una pila (LIFO) usando una lista."""

    def __init__(self):
        self.items = []

    def push(self, value):
        """Apila un elemento."""
        self.items.append(value)

    def pop(self):
        """Desapila y devuelve el elemento tope. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La pila está vacía")
        return self.items.pop()

    def peek(self):
        """Devuelve el elemento tope sin desapilar. Retorna None si está vacía."""
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def __len__(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)