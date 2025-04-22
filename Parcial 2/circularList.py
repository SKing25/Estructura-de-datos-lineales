class CircularList:
    """Implementación de una lista circular con capacidad fija."""

    def __init__(self, capacity):
        """Inicializa la lista con la capacidad especificada."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def insert(self, value):
        """Inserta un valor al final. Lanza excepción si está llena."""
        if self.is_full():
            raise Exception("La lista circular está llena")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def delete(self):
        """Elimina y devuelve el elemento del frente. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La lista circular está vacía")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.size == 0

    def is_full(self):
        """Verifica si la lista está llena."""
        return self.size == self.capacity

    def __len__(self):
        """Devuelve el número de elementos en la lista."""
        return self.size