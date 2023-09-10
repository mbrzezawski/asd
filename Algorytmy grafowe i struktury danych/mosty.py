def find_bridges(G):
    inf = float('inf')
    time = 0
    n = len(G) 
    d = [inf] * n
    low = [inf] * n
    visited = [False] * n
    parent = [-1] * n
    result = []
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, parent, low, d, time, G, result)
    return result

def dfs(u, visited, parent, low, d, time, G, result):
    visited[u] = True
    d[u] = time
    low[u] = time
    time += 1

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v, visited, parent, low, d, time, G, result)

            low[u] = min(low[u], low[v])
            if low[v] == d[v]:
                x = u, v
                result.append(x)

        elif v!= parent[u]:
            low[u] = min(low[u], d[v])

graph = [ [ 1, 2],
          [ 0, 2],
          [ 0, 1, 3],
          [ 2, 4, 5],
          [ 3, 5],
          [ 3, 4] ]
print(find_bridges(graph))