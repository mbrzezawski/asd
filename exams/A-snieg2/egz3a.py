from egz3atesty import runtests

def snow( T, I ):
    n = len(I)
    data = []

    for i in range(n):
        data.append((I[i][0], "x"))
        data.append((I[i][1], "y"))
    data = sorted(data, key=lambda x : x[0])
    count = 0
    best = 0
    for i in range(len(data)):
        if data[i][1] == "x":
            count += 1
        if data[i][1] == "y":
            count -= 1
        
        best = max(best, count)

    return best
                     

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
