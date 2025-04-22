**DESCRIPCIÓN DEL PROYECTO**  
Este proyecto implementa estructuras de datos (listas circulares, pilas, colas, árboles binarios) y algoritmos de ordenamiento/búsqueda en Python. Incluye un script interactivo (`main.py`) que demuestra su funcionamiento con datos ingresados por el usuario.

**COMPONENTES DEL CÓDIGO**  

1. **Estructuras de Datos**:  
   - `circular_list.py`: Lista circular con capacidad fija (métodos: `insert`, `delete`, `is_empty`, `is_full`).  
   - `stack.py`: Pila (LIFO) con `push`, `pop`, `peek`.  
   - `queue.py`:  
     - `Queue`: Cola FIFO básica.  
     - `PriorityQueue`: Cola de prioridad (usa `heapq`).  
     - `Deque`: Bicola (operaciones front/rear).  
     - `CircularQueue`: Cola circular con buffer fijo.  
   - `bst.py`: Árbol binario de búsqueda (inserción, recorrido in-order, altura).  

2. **Algoritmos**:  
   - `sorting.py`:  
     - `merge_sort`: Ordenamiento por mezcla (devuelve nueva lista).  
     - `quick_sort`: Ordenamiento rápido in-place.  
   - `searching.py`:  
     - `linear_search`: Búsqueda lineal (O(n)).  
     - `binary_search`: Búsqueda binaria (O(log n), requiere lista ordenada).  

3. **Script Principal**:  
   - `main.py`:  
     - Lee una lista de enteros desde la consola.  
     - Demuestra todas las estructuras y algoritmos.  
     - Muestra resultados ordenados y búsquedas.

**CÓMO SE USA EL CÓDIGO**  

1. **Para el usuario final**:  
   - Ejecuta `main.py`, ingresa números separados por comas (ej: `5,3,8,1,9,2`).  
   - El script automáticamente:  
     - Crea una lista circular con los datos.  
     - Apila/desapila elementos con una pila.  
     - Encola/desencola elementos con una cola FIFO.  
     - Ordena la lista con Merge Sort y Quick Sort.  
     - Busca un valor ingresado con ambos algoritmos de búsqueda.  
     - Construye un árbol binario y muestra su recorrido in-order y altura.  

2. **Para desarrolladores**:  
   - Importa las clases/algoritmos desde los módulos (ej: `from queue import PriorityQueue`).  
   - Usa los métodos según sea necesario (ej: `pq.enqueue(valor, prioridad)`).  

3. **Ejemplo de salida**:  
   ```plaintext  
   --- Lista Original ---  
   Entrada: [5, 3, 8, 1, 9, 2]  

   --- Pila ---  
   Desapilados (2): [8, 3]  

   --- Árbol Binario ---  
   Recorrido In-Order: [1, 2, 3, 5, 8, 9]  
   Altura del árbol: 3  
   ```