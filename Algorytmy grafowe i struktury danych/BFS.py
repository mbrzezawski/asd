from collections import deque

# V + E
def BFS_list(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    d = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while len(queue) != 0:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
    return d, parent
    
# V^2
def BFS_matrix(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    d = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()
        for v, edge in enumerate(G[u]):
            if not visited[v] and edge == 1:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
    return d, parent

graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6]]

print(BFS_list(graph, 0))