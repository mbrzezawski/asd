def podziel(T, start, end):
    pivot = T[end]
    low = start
    high = end - 1

    while True:
        while low <= high and T[low] <= pivot:
            low += 1
        
        while low <= high and T[high] >= pivot:
            high -= 1

        if low <= high:
            T[low], T[high] = T[high], T[low]
        else:
            break
    T[end], T[low] = T[low], T[end]
    return low

def quicksort(T, start, end):
    if start < end:
        pivot = podziel(T, start, end)
        quicksort(T, start, pivot - 1)
        quicksort(T, pivot + 1, end)
    return T

T = [1, 3, 2, 5, 8, 4, 5]
print(quicksort(T,0,len(T) - 1))