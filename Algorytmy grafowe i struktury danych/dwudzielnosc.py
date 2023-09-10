def isBipartite(G, src):
    n = len(G)
    colorArr = [-1] * n
 
        
    colorArr[src] = 1
 
        
    queue = []
    queue.append(src)
 
        
    while queue:
 
        u = queue.pop()
 
        for v in range(n):
 
                
            if G[u][v] and colorArr[v] == -1:
                    
                colorArr[v] = 1 - colorArr[u]
                queue.append(v)
 
                
            elif G[u][v] and colorArr[v] == colorArr[u]:
                return False
 
        
    return True