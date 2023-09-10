from queue import PriorityQueue
# lista
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

