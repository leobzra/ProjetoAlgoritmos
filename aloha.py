git commit -m "meu primeiro commit"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        mst = []
        visited = [False] * self.V
        key = [float('inf')] * self.V
        parent = [-1] * self.V

        key[0] = 0  # Start from vertex 0

        for _ in range(self.V):
            min_key = float('inf')
            u = None

            for v in range(self.V):
                if not visited[v] and key[v] < min_key:
                    min_key = key[v]
                    u = v

            visited[u] = True

            for v, weight in self.graph[u]:
                if not visited[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u

        for v in range(1, self.V):
            mst.append((parent[v], v, key[v]))

        return mst

