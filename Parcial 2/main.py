# main.py
from circularList import CircularList
from stack import Stack
from queues import Queue
from sorts import merge_sort, quick_sort
from searches import linear_search, binary_search
from binaryTrees import BinarySearchTree

def main():
    # Leer entrada del usuario
    user_input = input("Ingrese una lista de enteros separados por comas: ")
    numbers = [int(num.strip()) for num in user_input.split(",")]
    print("\n--- Lista Original ---")
    print(f"Entrada: {numbers}")

    # 1. Lista Circular
    circular = CircularList(len(numbers))
    for num in numbers:
        circular.insert(num)
    print("\n--- Lista Circular ---")
    print(f"Elementos insertados: {numbers}")
    print(f"Tamaño actual: {len(circular)}")

    # 2. Pila (primeros 3 elementos, desapilar 2)
    stack = Stack()
    for num in numbers[:3]:
        stack.push(num)
    popped = []
    for _ in range(2):
        try:
            popped.append(stack.pop())
        except Exception as e:
            print(f"Error: {e}")
    print("\n--- Pila ---")
    print(f"Apilados (primeros 3): {numbers[:3]}")
    print(f"Desapilados (2): {popped}")
    print(f"Tamaño final: {len(stack)}")

    # 3. Cola FIFO (encolar todo, desencolar 2)
    queue = Queue()
    for num in numbers:
        queue.enqueue(num)
    dequeued = []
    for _ in range(2):
        try:
            dequeued.append(queue.dequeue())
        except Exception as e:
            print(f"Error: {e}")
    print("\n--- Cola FIFO ---")
    print(f"Desencolados (2): {dequeued}")
    print(f"Tamaño final: {len(queue)}")

    # 4. Ordenamiento
    sorted_merge = merge_sort(numbers.copy())
    quick_copy = numbers.copy()
    quick_sort(quick_copy, 0, len(quick_copy) - 1)
    print("\n--- Ordenamiento ---")
    print(f"Merge Sort: {sorted_merge}")
    print(f"Quick Sort: {quick_copy}")

    # 5. Búsqueda
    target = int(input("\nIngrese un valor a buscar: "))
    linear_idx = linear_search(numbers, target)
    binary_idx = binary_search(sorted_merge, target)
    print("\n--- Búsqueda ---")
    print(f"Lineal (índice): {linear_idx}")
    print(f"Binaria (índice en lista ordenada): {binary_idx}")

    # 6. Árbol Binario de Búsqueda
    bst = BinarySearchTree()
    for num in numbers:
        bst.insert(num)
    print("\n--- Árbol Binario ---")
    print(f"Recorrido In-Order: {bst.in_order_traversal()}")
    print(f"Altura del árbol: {bst.height()}")

if __name__ == "__main__":
    main()