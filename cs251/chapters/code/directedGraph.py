from heapq import heappush, heappop
from collections import deque


class Graph:
    # e.g.,: Graph(n = 3, edges = [[0,1],[1,2],[0,2]])
    # creates a graph with 3 nodes indexed 0, 1, 2,
    # with 0 -> 1, 0 -> 2, 1 -> 2
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]
        for u, v in edges:
            self.adjList[u].append(v)

        self.adjMatrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(v):
            self.adjMatrix[i][i] = 0
        for u, v in edges:
            self.adjMatrix[u][v] = 1

    # reference undirectedGraph.py for DFS examples
    def bfs(self, v: int):  # v is the starting node
        q = deque()
        dist = [-1] * self.n
        path = [[] for _ in range(self.n)]
        visited = [False] * self.n

        q.append(v)
        dist[v] = 0
        path[v] = [0]
        visited[v] = True

        while q:
            u = q.pop()

            for w in self.adjList[u]:
                if not visited[w]:
                    q.append(w)
                    dist[w] = dist[u] + 1
                    path[w] = path[u] + [w]
                    visited[w] = True

        return dist, path, visited

    def kahnTopologicalSort(self):
        indeg = [0] * self.n

        for u, v in self.edges:
            indeg[v] += 1

        q = deque()
        for v in range(self.n):
            if indeg[v] == 0:
                q.append(v)

        ordering = []
        while q:
            u = q.pop()
            ordering.append(u)

            for w in self.adjList[u]:
                indeg[w] -= 1  # "removing" the edge
                if indeg[w] == 0:
                    q.append(w)

        # if we do not have all the nodes in the ordering list,
        # it means that the graph is not DAG.
        # It is because if the graph is DAG, all nodes will eventually have
        # zero indegree after edge removal
        return [] if len(ordering) != self.n else ordering





def testTopologicalSort():
    # this graph is DAG
    graph = Graph(3, [[0, 1], [1, 2], [0, 2]])
    assert graph.kahnTopologicalSort() == [0, 1, 2]

    # this graph is not DAG
    graph = Graph(3, [[0, 1], [1, 2], [2, 0]])
    assert graph.kahnTopologicalSort() == []


testTopologicalSort()
