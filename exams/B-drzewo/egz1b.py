from egz1btesty import runtests
from queue import Queue
# do dokonczenia
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


index = 0
def index_graph(T):
    global index
    if T is not None:
        T.x = index
        index += 1
        index_graph(T.left)
        index_graph(T.right)


def bfs_dist(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    d = [0 for _ in range(len(G))]
    queue = Queue()
    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
    return d, parent


def bfs_delete(G, s, to_delete):
    to_delete_upper = 0
    visited = [False for _ in range(len(G))]
    queue = Queue()
    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if to_delete[v]:
                to_delete_upper += 1
            elif not visited[v]:
                queue.put(v)
                visited[v] = True
    return to_delete_upper


def count_nodes(T):
        if T is None:
            return 0
        return count_nodes(T.left) + count_nodes(T.right) + 1


def wideentall(T):
    global index
    n = count_nodes(T)
    graph = [[] for _ in range(n)]
    index = 0
    index_graph(T)

    def create_graph(T):
        if T.left is not None:
            graph[T.x].append(T.left.x)
            graph[T.left.x].append(T.x)
            create_graph(T.left)
        
        if T.right is not None:
            graph[T.x].append(T.right.x)
            graph[T.right.x].append(T.x)
            create_graph(T.right)
    
    create_graph(T)
    global parent
    dist_from_root, parent = bfs_dist(graph, 0)
    levels = [0 for _ in range(n)]

    for i in range(n):
        levels[dist_from_root[i]] += 1
    
    max_nodes = max(levels)
    for i in range(n - 1, -1, -1):
        if levels[i] == max_nodes:
            best_level = i
            break

    to_delete_lower = 0
    for i in range(n):
        if dist_from_root[i] == best_level + 1:
            to_delete_lower += 1
    
    global to_delete
    to_delete = [True for _ in range(n)]
    def delete_upper(node):
        global to_delete, parent
        to_delete[node] = False
        if node != 0:
            delete_upper(parent[node])
    
    for i in range(n):
        if dist_from_root[i] == best_level:
            delete_upper(i)
    

    to_delete_upper = bfs_delete(graph, 0, to_delete)
    
    return to_delete_lower + to_delete_upper


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )