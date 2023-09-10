def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return(distance)

