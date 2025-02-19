import heapq
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.dense import reconstruct_path


def a_star_with_visualization(G, start, goal, heuristic):
    """
    Implementacion del algoritmo A* sobre el grafo G,
    dada la heuristicapara cada nodo.
    Devuelve el camino desde 'start' hasta el 'goal' (si existe)
    """

    #cola de prioridad: cada elemento es (costo_estimado, nodo)
    open_list = []
    heapq.heappush(open_list, (0, start))

    #Diccionarios para guardad el costo real y el camino recorrido
    cost_so_far = {start: 0}
    came_from = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        #si llegamos al objetivo, recostruimos el camino
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in G.neighbors(current):
            #Costo de las aristas en G (en ese ejemplo, asumimos 'peso' en un atributo)
            edge_weight = G[current][neighbor].get('weight', 1)
            new_cost = cost_so_far[current] + edge_weight

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current
    return None #si no se encuentra camino

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

#Creamos un grafo con pesos simulando distancias
H = nx.Graph()
H.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'D', 2),
    ('C', 'D', 1),
    ('D', 'E', 5),
    ('C', 'F', 4),
    ('F', 'E', 2),
])

#Heuristica aproximada (ficticia) para cada nodo (distancia estimada a 'E'
heuristic = {
    'A':6,
    'B':4,
    'C':3,
    'D':2,
    'E':0,
    'F':2,
}

start_node = 'A'
goal_node = 'E'
path = a_star_with_visualization(H, start_node, goal_node, heuristic)

#Visualizacion del grafo y el camino resultante
pos = nx.spring_layout(H, seed=42)

plt.figure(figsize=(8, 6))

# 1) Dibujamos nodos y etiquetas normalmente
nx.draw_networkx_nodes(H, pos, node_color='lightblue', node_size=800)
nx.draw_networkx_labels(H, pos, font_weight='bold')

# 2) Dibujamos todas las aristas en negro
nx.draw_networkx_edges(H, pos, edge_color='black')

# 3) si A* encontro un camino, resaltamos sus aristas en rojo
if path:
    #Generamos pares consecutivos (u, v) para remarcar el camino
    path_edges = list(zip(path, path[1:]))

    nx.draw_networkx_edges(
        H, pos,
        edgelist = path_edges,
        edge_color = 'red',
        width=3,
    )
    plt.title(f"Camino encontrado por A*: {'->'.join(path)}", fontsize=12)
else:
    plt.title("No se encontro un camino", fontsize=12)

#Mostramos cada arista
edge_labels = nx.get_edge_attributes(H, 'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
