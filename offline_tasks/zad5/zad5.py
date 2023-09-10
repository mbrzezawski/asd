# Maciej Brzeżawski
# Do rozwiązania zadania posłużyłem się implementacją algorytmu Dijkstry, który pozwolił mi znaleźć najkrótszą ścieżkę w grafie ważonym.
# Stworzyłem graf G (reprezentowany jako lista sąsiedzstwa) do którego przypisałem krawędzie między danymi wierzchołkami wraz z ich wagami z tablicy E. 
# Następnie do grafu G przypisałem krawędzie tym razem z tablicy S, ale o wadze 0 ponieważ koszt przejścia między nimi jest 'darmowy'.
# Potem pozostało już tylko wywołać algorytm Dijkstry i zwrócić długość najkrótszej ścieżki. Złożoność algorytmu to O(E+S^2+ElogV).

from zad5testy import runtests
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    inf = float('inf')
    parents = [None] * n
    weights = [inf] * n
    pq = PriorityQueue()
    weights[s] = 0
    pq.put((0, s))
    
    while not pq.empty():
        _, u = pq.get()
        for v, weight in G[u]:
            if weights[u] + weight < weights[v]:
                weights[v] = weights[u] + weight
                parents[v] = u
                pq.put((weights[v], v))
        
    return parents, weights

def spacetravel( n, E, S, a, b ):
    G =[[] for i in range(n)]
    
    for i in range(len(E)):
        l = (E[i][0])
        x = (E[i][1])
        y = (E[i][2])
        z = x, y
        o = l, y
        G[E[i][0]].append(z)
        G[E[i][1]].append(o)
    
    for j in range(len(S)):
        for k in range(len(S)):
            if j != k:
                p = S[k]
                w = 0
                c = p, w
                G[S[j]].append(c)

    G_dijkstra = dijkstra(G, a)

    if G_dijkstra[1][b] == float('inf'):
        return None
    return G_dijkstra[1][b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )