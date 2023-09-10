def bubblesort(T):
    n = len(T)
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(n - 1):
            if T[i] > T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
                sorted = False
    return T

T = [1, 3, 2, 5, 8, 4, 5]
print(bubblesort(T))