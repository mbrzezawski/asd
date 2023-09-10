from math import inf

def relax(G, distance, parent, j, k):
    if distance[k[0]] > distance[j] + k[1]:
        distance[k[0]] = distance[j] + k[1]
        parent[k[0]] = j


def bellman_ford_algorithm(G, source):
    n = len(G)
    
    distance = [inf] * (n)
    parent = [None] * (n)
    distance[source] = 0
    for i in range(n - 1):
        for j in range(n):
            for k in G[j]:
                relax(G, distance, parent, j, k)
    
    return distance, parent

# zamiana E = [0, 1, 6]... na liste sasiedzstwa ...G[0] = (1, 6)
def zmiana(E, G):
    for i in range(len(E)):
        x = (E[i][0])
        y = (E[i][1])
        z = (E[i][2])
        w = y, z
        o = x, z
        G[E[i][0]].append(w)
        G[E[i][1]].append(o)
    return G

# zamiana G[0] = (1,6) na E = [0, 1, 6]
def zamiana(G, E):
    for i in range(len(G)):
        for j in range(len(G[i])):
            x = (i, G[j][0], G[j][1])
            E.append(x) 
    return E
    