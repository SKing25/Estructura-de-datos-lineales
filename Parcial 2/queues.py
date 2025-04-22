import heapq

class Queue:
    """Implementación básica de una cola FIFO."""

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        """Encola un elemento."""
        self.items.append(value)

    def dequeue(self):
        """Desencola y devuelve el primer elemento. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La cola está vacía")
        return self.items.pop(0)

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def __len__(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.items)

class PriorityQueue:
    """Cola de prioridad (menor valor = mayor prioridad). Usa heapq."""

    def __init__(self):
        self.heap = []
        self.size = 0

    def enqueue(self, value, priority):
        """Encola un elemento con su prioridad."""
        heapq.heappush(self.heap, (priority, value))
        self.size += 1

    def dequeue(self):
        """Desencola el elemento de mayor prioridad. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La cola de prioridad está vacía")
        self.size -= 1
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return self.size == 0

    def __len__(self):
        """Devuelve el número de elementos en la cola."""
        return self.size

class Deque:
    """Implementación de una bicola."""

    def __init__(self):
        self.items = []

    def add_front(self, value):
        """Añade un elemento al frente."""
        self.items.insert(0, value)

    def add_rear(self, value):
        """Añade un elemento al final."""
        self.items.append(value)

    def remove_front(self):
        """Elimina y devuelve el elemento del frente. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La bicola está vacía")
        return self.items.pop(0)

    def remove_rear(self):
        """Elimina y devuelve el elemento del final. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La bicola está vacía")
        return self.items.pop()

    def is_empty(self):
        """Verifica si la bicola está vacía."""
        return len(self.items) == 0

    def __len__(self):
        """Devuelve el número de elementos en la bicola."""
        return len(self.items)

class CircularQueue:
    """Cola circular con capacidad fija."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        """Encola un elemento. Lanza excepción si está llena."""
        if self.is_full():
            raise Exception("La cola circular está llena")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        """Desencola y devuelve el primer elemento. Lanza excepción si está vacía."""
        if self.is_empty():
            raise Exception("La cola circular está vacía")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return self.size == 0

    def is_full(self):
        """Verifica si la cola está llena."""
        return self.size == self.capacity

    def __len__(self):
        """Devuelve el número de elementos en la cola."""
        return self.size