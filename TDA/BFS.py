import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs_with_levels(G, start):
    """
    Realiza un recorrido en anchura (BFS) sobre el grafo 'G',
    iniciando en el nodo 'start'

    Retorna:
    - visited_order: Lista con los nodos en el orden en que fueron visitados
    - Level: Diccionario que indica el "nivel" de cada nodo
    (distancia minima en aristas desde el nodo de inicio)
    """

    visited_order = []
    level = {}
    visited = set()

    #cola para BFS, inicia con el nodo de comienzo
    queue = deque([start])
    visited.add(start)
    level[start] = 0

    while queue:
        current_node = queue.popleft()
        visited_order.append(current_node)

        #iteramos sobre todos los vecinos del nodo actual
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                #asignamos el nivel al vecino (nivel del padre + 1)
                level[neighbor] = level[current_node] + 1

    return visited_order, level


# 1) Crear un grafo de ejemplo
G = nx.DiGraph()
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'F'),
    ('E', 'F'),
]
G.add_edges_from(edges)

# 2) Ejecutar BFS desde un nodo inicial, por ejemplo 'A'
start_node = 'A'
visited_order, levels = bfs_with_levels(G, start_node)

# 3) Visualizacion del grafo y del orden de vista

# posicionamos los nodos para el dibujo (layout)
pos = nx.spring_layout(G, seed=42)

# - El "nivel" de cada nodo se usara para colorearlo
# Mientras mas pequeño el nivel, mas claro el color (o viceversa)
node_levels = [levels[n] for n in G.nodes()]

plt.figure(figsize = (8,6))

#Dibujamos los nodos y les asignamos un color segun su nivel
nodes = nx.draw_networkx_nodes(
    G,
    pos,
    node_color = node_levels,
    cmap = plt.cm.Blues,
    node_size = 800
)

#Dibujamos las aristas
nx.draw_networkx_edges(
    G,
    pos,
    edge_color = "gray"
)

#Agregamos un titulo con el orden de la visita
plt.title(
    f"BFS desde un nodo {start_node}\n"
    f"Orden de la visita: {visited_order}\n"
    f"Niveles de cada nodo: {levels}"
)

#Barra de color para ver la escala de niveles
cbar = plt.colorbar(nodes)
cbar.set_label("Nivel (Distancia en BFS)")

plt.axis('off')
plt.show()