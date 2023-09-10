from zad6testy import runtests
from math import inf


def dfs_visit(graph, source, visited, parent):
    visited[source] = True
    for v in range(len(graph)):
        if not visited[v] and graph[source][v] != 0:
            parent[v] = source
            dfs_visit(graph, v, visited, parent)


def dfs(graph, s, t, parent):
    visited = [False] * len(graph)
    dfs_visit(graph, s, visited, parent)
    return visited[t]


def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while dfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow

def binworker( M ):

    G = [[0 for _ in range(2 * len(M) + 2)] for _ in range(2 * len(M) + 2)]
    
    for i in range(len(M)):
        G[0][i+1] = 1
        G[len(M) + 1 + i][2*len(M) + 2 - 1] = 1
    for i in range(len(M)):
        m = len(M[i])
        for j in range(m):
            G[i+1][M[i][j] + len(M) + 1] = 1
    x = edmonds_karp_algorithm(G, 0, 2 * len(M) + 2 - 1)
    return x
#M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
#print(binworker(M))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
