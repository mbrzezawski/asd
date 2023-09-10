# Maciej Brzeżawski
# Do rozwiązania zadania posłużyłem się dwoma implementacjami algorytmu Dijkstry. W jednym z nich dodałem linijkę, która daną wagę
# wierzchołka mnoży x2 i dodaje wartość 'r'. Następnie dla wierzchołka t wywołuję zmieniony algorytm Dijkstry. 
# Pozostało tylko sprawdzić czy opłaca nam się 'napaść' na dany zamek (wierzchołek), w tym celu sprawdzamy czy koszt dotychczasowej 
# drogi do wierzchołka i-tego z wierzchołka s plus koszt drogi już w zmienionym grafie (z dodanymi wagami w drugim algorytmie Dijkstry) 
# do wierzchołka t minus V[i] (złoto w zamku) jest najmniejszy. Szacowana złożoność algorytmu O(V^2logV).
from egz1Atesty import runtests
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

def dijkstrachanged(G, s, r):
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
            weight = weight * 2 + r
            if weights[u] + weight < weights[v]:
                weights[v] = weights[u] + weight
                parents[v] = u
                pq.put((weights[v], v))
    return parents, weights

def gold(G,V,s,t,r):
    best = float('inf')
    a, b = dijkstra(G, s)
    c, d = dijkstrachanged(G, t, r)
    for i in range(len(V)):
        if b[i] + d[i] - V[i] < best:
            best = b[i] + d[i] - V[i]

    return best 

runtests( gold, all_tests = True )
