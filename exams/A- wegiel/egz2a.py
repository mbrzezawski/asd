from egz2atesty import runtests
# wzorcowe drzewa przedziałowe 
def coal( A, T ):
    n = len(A)
    M = [T for _ in range(n)]
    inx = None
    for i in range(n):
        for j in range(n):
            if M[j] - A[i] >= 0:
                M[j] -= A[i]
                inx = j
                break
    return inx

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True)
