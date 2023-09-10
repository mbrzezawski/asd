from zad2testy import runtests
# Maciej Brzeżawski
# W celu rozwiązania zadania posłużyłem się implementacją algorytmu sortowania przez kopcowanie. 
# Zaobserwowałem, że od pewnego momentu wartość śniegu na danym indeksie minus indeks jest mniejsza od 0 więc tych wartości nie warto sortować,
# ponieważ i tak nie zostaną dodane do całkowitej liczby śniegu. Zauważmy, że w pierwszym dniu (i = n-1) odejmiemy 0 śniegu, w następnym (i = n-2) 1 śniegu itd.
# Z tego faktu możemy wywnioskować warunek sortowania, który odpowiada nam na pytanie czy opłaca nam się zamieniać T[0] z T[i], jeśli tego nie zrobimy,
# wartość śniegu pod tym indeksem nie będzie brana pod uwagę podczas sortowania.  W posortowanej oraz odwrócnej tablicy przechodziłem po indeksach
# tak długo jak wartośc śniegu pod danym indeksem minus indeks (indeks symbolizuje liczbę dni) jest większa od 0 i dodawałem tę wartość do całkowitej sumy śniegu.
# Złożonośc algorytmu to O(nlogn).

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i-1)//2

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
        heapify(T, max_ind, n)

def buildheap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, i, n)

def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n-1, 0, -1):
        if T[0] - (n - i - 1) > 0:
            T[0], T[i] = T[i], T[0]
            heapify(T, 0, i)
    return T

def snow( S ):
    heapsort(S)
    S = S[::-1]
    ammount_of_snow = 0
    i = 0
    while S[i] - i > 0:
        ammount_of_snow += S[i] - i
        i += 1
    return ammount_of_snow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
