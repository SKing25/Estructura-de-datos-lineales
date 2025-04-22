#
"""
**Ejercicio 2: **
Implementación de Recorridos en un Árbol Binario​
Objetivo: Practicar la escritura de algoritmos recursivos para recorrer un árbol.​
Actividad:​
Escribe el pseudocódigo para implementar los siguientes recorridos:​
Recorrido Preorden: Visitar la raíz, el subárbol izquierdo y el subárbol derecho.​
Recorrido Inorden: Visitar el subárbol izquierdo, la raíz y luego el subárbol derecho.​
Recorrido Postorden: Visitar el subárbol izquierdo, el subárbol derecho y finalmente la raíz.​
Implementa cada uno de estos recorridos en el lenguaje de programación de tu preferencia y prueba tu código con el árbol dibujado en el Ejercicio 1.

Función RecorrerArbol(nodo, tipo):
    Si nodo es null:
        Retornar

    Si tipo es "preorden":
        Visitar nodo
        RecorrerArbol(nodo.izquierdo, tipo)
        RecorrerArbol(nodo.derecho, tipo)

    Si tipo es "inorden":
        RecorrerArbol(nodo.izquierdo, tipo)
        Visitar nodo
        RecorrerArbol(nodo.derecho, tipo)

    Si tipo es "postorden":
        RecorrerArbol(nodo.izquierdo, tipo)
        RecorrerArbol(nodo.derecho, tipo)
        Visitar nodo

**Pseudocodigo(Implementado en Python):**
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Implementación de los recorridos

# Recorrido Preorden (Raíz, Izquierda, Derecha)
def preorden(nodo):
    if nodo is None:
        return
    print(nodo.valor, end=" ")  # Visitar nodo
    preorden(nodo.izquierdo)    # Recorrer subárbol izquierdo
    preorden(nodo.derecho)      # Recorrer subárbol derecho

# Recorrido Inorden (Izquierda, Raíz, Derecha)
def inorden(nodo):
    if nodo is None:
        return
    inorden(nodo.izquierdo)     # Recorrer subárbol izquierdo
    print(nodo.valor, end=" ")  # Visitar nodo
    inorden(nodo.derecho)       # Recorrer subárbol derecho

# Recorrido Postorden (Izquierda, Derecha, Raíz)
def postorden(nodo):
    if nodo is None:
        return
    postorden(nodo.izquierdo)   # Recorrer subárbol izquierdo
    postorden(nodo.derecho)     # Recorrer subárbol derecho
    print(nodo.valor, end=" ")  # Visitar nodo

# Creación del árbol binario
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

# Este es un ejemplo de uso de los recorridos

print("Recorrido Preorden:")
preorden(raiz)  # Salida esperada: 1 2 4 5 3 6 7
print("\nRecorrido Inorden:")
inorden(raiz)   # Salida esperada: 4 2 5 1 6 3 7
print("\nRecorrido Postorden:")
postorden(raiz) # Salida esperada: 4 5 2 6 7 3 1

# Juan Lozano

"""**Ejercicio 3: **
Inserción y Búsqueda en un Árbol Binario de Búsqueda (BST)​

Objetivo: Entender cómo se insertan elementos y se realizan búsquedas en un BST.​

Actividad:​

Inserción: Diseña un algoritmo que inserte un nuevo nodo en el BST manteniendo la propiedad de que para cada nodo, los valores del subárbol izquierdo son menores y los del derecho son mayores.​

Búsqueda: Escribe una función que reciba el valor buscado y recorra el BST para determinar si dicho valor existe en el árbol.​

Pista:​

Utiliza la recursividad para simplificar la implementación de ambos algoritmos.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para insertar un valor en el BST
def insertar(root, valor):
    if root is None:
        return Nodo(valor)

    # Si el valor es menor que el nodo actual, insertarlo en el subárbol izquierdo
    if valor < root.valor:
        root.izquierdo = insertar(root.izquierdo, valor)
    # Si el valor es mayor que el nodo actual, insertarlo en el subárbol derecho
    elif valor > root.valor:
        root.derecho = insertar(root.derecho, valor)

    return root

# Función para buscar un valor en el BST
def buscar(root, valor):
    # Si el nodo es null o el valor se encuentra en el nodo actual
    if root is None or root.valor == valor:
        return root

    # Si el valor es menor que el nodo actual, buscar en el subárbol izquierdo
    if valor < root.valor:
        return buscar(root.izquierdo, valor)

    # Si el valor es mayor que el nodo actual, buscar en el subárbol derecho
    return buscar(root.derecho, valor)

# Crear el árbol binario de búsqueda
raiz = Nodo(50)  # Raíz inicial

# Insertar elementos en el árbol
valores = [30, 20, 40, 70, 60, 80]
for valor in valores:
    raiz = insertar(raiz, valor)

# Probar búsqueda de un valor existente
valor_a_buscar = 40
resultado = buscar(raiz, valor_a_buscar)
if resultado:
    print(f"Valor {valor_a_buscar} encontrado en el árbol.")
else:
    print(f"Valor {valor_a_buscar} no encontrado en el árbol.")

# Probar búsqueda de un valor no existente
valor_a_buscar = 25
resultado = buscar(raiz, valor_a_buscar)
if resultado:
    print(f"Valor {valor_a_buscar} encontrado en el árbol.")
else:
    print(f"Valor {valor_a_buscar} no encontrado en el árbol.")


# Juan Lozano

"""**Ejercicio 4:**
Cálculo de la Altura de un Árbol Binario​

Objetivo: Determinar la profundidad máxima de un árbol, lo cual es clave para entender su balance y eficiencia.​

Actividad:​

Escribe una función recursiva que calcule la altura de un árbol binario.​

Define la altura como el número de nodos en el camino más largo desde la raíz hasta una hoja (o usa la convención que consideres adecuada, por ejemplo, que el árbol vacío tenga altura -1 o 0).

**Pseudocodigo(El de la diapositiva)**

function altura(nodo):
  if nodo == null:
    return 0 // 0 - 1 según la convención
  else:
    altIzq = altura(nodo.izquierdo)
    alrDer = altura(nodo.derecho)
    return max(altIzq, altDer) + 1
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función recursiva para calcular la altura de un árbol binario
def altura(nodo):
    # Si el nodo es None (árbol vacío), se retorna 0
    if nodo is None:
        return 0

    # Calcular la altura de los subárboles izquierdo y derecho
    altIzq = altura(nodo.izquierdo)
    altDer = altura(nodo.derecho)

    # La altura del nodo es el máximo entre los dos subárboles + 1 (para el nodo actual)
    return max(altIzq, altDer) + 1

# Crear un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

# Calcular la altura del árbol
print("La altura del árbol es:", altura(raiz))


# Juan Lozano

"""**Ejercicio 5: **

Verificar si un Árbol es un Árbol de Búsqueda Binario (BST)​

Objetivo: Determinar si un árbol binario cumple con la propiedad de un BST.​

Actividad:​

Diseña un algoritmo que recorra el árbol y verifique, para cada nodo, que los valores en el subárbol izquierdo sean menores y los del subárbol derecho sean mayores.​

Considera usar rangos (valores mínimos y máximos permitidos) para cada llamada recursiva, lo cual es una técnica eficiente para esta verificación.​

Pista: Puedes utilizar el siguiente enfoque en pseudocódigo:

**Pseudocodigo:**

function esBST(nodo, min, max):
  if nodo == null:
    return true
  if nodo.valor <= min or nodo.valor >= max:
    return false
  return esBST(nodo.izquierdo, min, nodo.valor) and esBST(nodo.derecho, nodo.valor, max)
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para verificar si el árbol es un BST
def esBST(nodo, min_val, max_val):
    # Si el nodo es None, es válido
    if nodo is None:
        return True

    # Verificar que el valor del nodo esté dentro del rango permitido
    if nodo.valor <= min_val or nodo.valor >= max_val:
        return False

    # Verificar recursivamente los subárboles izquierdo y derecho
    return esBST(nodo.izquierdo, min_val, nodo.valor) and esBST(nodo.derecho, nodo.valor, max_val)

# Crear un árbol de ejemplo
raiz = Nodo(50)
raiz.izquierdo = Nodo(30)
raiz.derecho = Nodo(70)
raiz.izquierdo.izquierdo = Nodo(20)
raiz.izquierdo.derecho = Nodo(40)
raiz.derecho.izquierdo = Nodo(60)
raiz.derecho.derecho = Nodo(80)

# Verificar si el árbol es un BST
if esBST(raiz, float('-inf'), float('inf')):
    print("El árbol es un Árbol de Búsqueda Binario (BST).")
else:
    print("El árbol NO es un Árbol de Búsqueda Binario (BST).")

# Juan Lozano

"""**Ejercicio 6: **
Recorrido por Niveles (BFS) de un Árbol Binario​

Objetivo: Implementar un recorrido que visite los nodos nivel por nivel, lo que es útil para visualizar la estructura del árbol.​

Actividad:​

Escribe un algoritmo que utilice una cola para recorrer el árbol binario en anchura (BFS).​

El algoritmo debe imprimir los valores de cada nodo en el orden en que se visitan.

Pseudocodigo:

funcion recorridorPorNiveles(raiz):
  if raiz == null:
    return
  cola = nueva Cola()
  cola.encolar(raiz)
  while not cola.estaVacia():
    nodo = cola.desencolar()
    imprimir(nodo.valor)
    if nodo.izquierdo != null:
      cola.encolar(nodo.izquierdo)
    if nodo.derecho != null:
      cola.encolar(nodo.derecho)
"""

from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para realizar el recorrido por niveles (BFS) en un árbol binario
def recorridoPorNiveles(raiz):
    if raiz is None:
        return

    # Crear una cola para almacenar los nodos por nivel
    cola = deque()
    cola.append(raiz)

    # Mientras la cola no esté vacía, procesar el siguiente nodo
    while cola:
        nodo = cola.popleft()  # Obtener el nodo en el frente de la cola
        print(nodo.valor, end=" ")  # Imprimir el valor del nodo

        # Encolar el hijo izquierdo, si existe
        if nodo.izquierdo:
            cola.append(nodo.izquierdo)

        # Encolar el hijo derecho, si existe
        if nodo.derecho:
            cola.append(nodo.derecho)

# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

# Realizar el recorrido por niveles
print("Recorrido por niveles (BFS) del árbol:")
recorridoPorNiveles(raiz)

# Juan Lozano