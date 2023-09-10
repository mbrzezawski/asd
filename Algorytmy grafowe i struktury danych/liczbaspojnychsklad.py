def ccs(G):
    vis = [0] * len(G)
    def DFS(v):
        vis[v] = 1
        for x in G[v]:
            if vis[x]:
                DFS[x]
    l = 0
    for i in range(len(G)):
        if not vis[i]:
            l += 1
            DFS(i)
    return l