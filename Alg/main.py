import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

file_path = 'distancias.xls' 
df = pd.read_excel(file_path, header=None, skiprows=2)  

vertices = df.iloc[:, 0].tolist()

graph = {vertex: {} for vertex in vertices}

for i, row in enumerate(df.iterrows(), start=1):
    vertex1 = vertices[i - 1]
    for j, distance in enumerate(row[1].tolist(), start=1):
        if pd.notna(distance) and isinstance(distance, (int, float)) and distance > 0:
            vertex2 = vertices[j - 1]
            graph[vertex1][vertex2] = distance
            graph[vertex2][vertex1] = distance

for vertex, neighbors in graph.items():
    print(f"{vertex} -> {neighbors}")


num_vertices = len(graph)
num_arestas = sum(len(neighbors) for neighbors in graph.values())
print(f"Número de vértices no Grafo: {num_vertices}")
print(f"Número de arestas no Grafo: {num_arestas}")

def prim(graph):
    start_vertex = vertices[0]
    visited = {vertex: False for vertex in vertices}
    distances = {vertex: float('inf') for vertex in vertices}
    parent = {vertex: None for vertex in vertices}

    distances[start_vertex] = 0

    for _ in range(len(vertices)):
        current_vertex = find_min_vertex(distances, visited)
        visited[current_vertex] = True

        for neighbor, weight in graph[current_vertex].items():
            if not visited[neighbor] and weight < distances[neighbor]:
                distances[neighbor] = weight
                parent[neighbor] = current_vertex

    mst = {vertex: {} for vertex in vertices}
    for vertex, par in parent.items():
        if par is not None:
            mst[vertex][par] = distances[vertex]
            mst[par][vertex] = distances[vertex]

    return mst


def find_min_vertex(distances, visited):
    min_vertex = None
    min_distance = float('inf')

    for vertex in distances:
        if not visited[vertex] and distances[vertex] < min_distance:
            min_vertex = vertex
            min_distance = distances[vertex]

    return min_vertex

G = nx.Graph()
for vertex, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(vertex, neighbor, weight=weight)

minimum_spanning_tree = prim(graph)


for vertex, neighbors in minimum_spanning_tree.items():
    for neighbor, weight in neighbors.items():
        print(f"{vertex} - {neighbor}: {weight}")

num_vertices = len(minimum_spanning_tree)
num_arestas = sum(len(neighbors) for neighbors in minimum_spanning_tree.values()) // 2
print(f"Número de vértices na Árvore Geradora Mínima: {num_vertices}")
print(f"Número de arestas na Árvore Geradora Mínima: {num_arestas}")

G = nx.Graph()
for vertex, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(vertex, neighbor, weight=weight)

pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
