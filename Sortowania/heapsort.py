#sortowanie kopcowe

def left(i):
    return 2 * i + 1

def right(i):
    return 2* i + 2

def parent(i):
    return (i-1) // 2 

# przywracanie własnosci kupca

def heapify(T, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T,max_ind, n)

# budowanie kopca

def bulidheap(T):
    n = len(T)
    for i in range(parent(n-1), -1 , -1):
        heapify(T, i, n)

# sortowanie kopca

def heapsort(T):
    n = len(T)
    bulidheap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)
    return T

T = [2, 1, 3, 6, 4, 3, 7, 1, 2]
print(heapsort(T))