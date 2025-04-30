from heapq import heappush, heappop


class Graph:
    # e.g.,: Graph(n = 3, edges = [[0,1,3],[1,2,1],[0,2,6]])
    # creates a graph with 3 nodes indexed 0, 1, 2,
    # with 0 -> 1 (weight 3), 0 -> 2 (weight 6), 1 -> 2 (weight 1)
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]
        for u, v, weight in edges:
            self.adjList[u].append((v, weight))

        self.adjMatrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(v):
            self.adjMatrix[i][i] = 0
        for u, v, w in edges:
            self.adjMatrix[u][v] = weight

    def dijkstra(self, v):
        dist = [float("inf")] * self.n
        prev = [None] * self.n

        dist[v] = 0
        q = [(0, v)]

        while q:
            priority, u = heappop(q)

            if priority == dist[u]:
                for w, weight in self.adjList[u]:
                    candidate = dist[u] + weight
                    if candidate < dist[w]:
                        dist[w] = candidate
                        prev[w] = u
                        heappush(q, (candidate, w))

        return dist, prev

    def floydWarshall(self):
        dist = [row[:] for row in self.adjMatrix]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist


def testDijkstra():
    graph = Graph(n=3, edges=[[0, 1, 3], [1, 2, 1], [0, 2, 6]])
    dist, prev = graph.dijkstra(0)
    assert dist == [0, 3, 6]
    assert prev == [None, 0, 0]


#def testFloydWarshall():


testDijkstra()
# testFloydWarshall()
