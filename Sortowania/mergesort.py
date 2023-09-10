def mergesort(T):
    n = len(T)
    if n > 1:
        mid = n//2
        left = T[:mid]
        right = T[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                T[k] = left[i]
                i += 1
            else:
                T[k] = right[j]
                j +=1
            k += 1
        while i < len(left):
            T[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            T[k] = right[j]
            k += 1
            j += 1
        print(T)
T = [2, 5, 3, 8, 5, 10, 6]
mergesort(T)
