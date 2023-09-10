
def DFS(G):
    def DFSVisit(G,u, visited,parents, d):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time
        for v in G[u]:
            if not visited[v]: 
                parents[v] = u
                DFSVisit(G,v,visited,parents, d)
                
    visited = [False for _ in range(len(G))]
    parents = [None for _ in range(len(G))]
    d = [-1 for _ in range(len(G))]
    time = 0

    for u in range(len(G)):
        if not visited[u]:
            DFSVisit(G,u,visited,parents, d)
    return parents, d
graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6]]
print(DFS(graph, 0))