def DFSEuler(G,u,S):
    n = len(G)
    
    for v in range(n):
        if G[u][v] == 1:
            G[u][v] = 0
            G[v][u] = 0
            S = DFSEuler(G,v,S)
    S.append(u)
    return S

def Checkifhascycle(G):
    n = len(G)
    for i in range(n):
            count = 0
            for j in range(n):
                if G[i][j] == 1:
                    count += 1
            if count%2 == 1:
                return False
    return True


G = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]
S = []
if Checkifhascycle(G): 
    S = DFSEuler(G,0,S)
    S.reverse
    print(S)