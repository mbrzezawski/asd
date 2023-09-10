# Maciej Brzeżawski
# Do rozwiązania zadania posłużyłem się implementacją algorytmu BFS. Na początku dzięki niemu znalazłem najkrótszą ścieżkę z wierzchołka s do t.
# Następnie przechodząc po znalezionej ścieżce po kolei usuwałem jej krawędzie i ponownie wykonywałem BFS na nowo utworzonym grafie z usuniętą krawędzią.
# Jeśli długość ścieżki w grafie z usniętą krawedzią była większa niż początkowo zapisana najkrótsza ścieżka oznaczało to, że znaleźliśmy krawędź, której szukaliśmy.
# Złożoność algorytmu O((V+E)*E).
from zad4testy import runtests
from collections import deque

def BFS(G, s):
    n = len(G)
    d = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    parent = [False for v in range(n)]
    Q = deque()
    d[s] = 0
    visited[s] = True
    parent[s] = None
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                visited[v] = True
                Q.append(v)
    return d, parent

def deledge(G,  u,  v):
    for i in range(len(G[u])):
        if (G[u][i] == v):       
            G[u].pop(i)
            break
    for i in range(len(G[v])):
        if (G[v][i] == u):
            G[v].pop(i)
            break
    return G

def longer( G, s, t ):
    bfs = BFS(G, s)
    parents = bfs[1]
    min_leng = bfs[0][t]

    if min_leng == -1:
        return None
    
    temp = t
    tempnext = parents[temp]

    while s != temp:
        G_copy = G
        G_copy = deledge(G_copy, temp, tempnext)
        bfs_copy = BFS(G, s)
        if bfs_copy[0][t] > min_leng or bfs_copy[0][t] == -1:
            return (temp, tempnext)
        temp = tempnext
        tempnext = parents[tempnext]
    
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )