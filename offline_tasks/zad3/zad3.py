# Maciej Brzeżawski
# Do rozwiązania zadania posłużyłem się implementacją algorytmu sortowania 'quicksort'. Przed posortowaniem tablicy zauważyłem, że 
# pierwsza litera odwrotności wyrazu kot (wyraz tok) jest 'większa' od ostatniej litery. Przez wielkość litery oznaczam jej odległość
# od początku alfabetu, im jest większa, to znajduję się dalej od pierwszej litery czyli a. Przeszedłem po tablicy wyrazów i każde take słowo
# odwróciłem dzięki czemu otrzymałem tablice z wyrazami bez ich odwrotności. Teraz pozostało już tylko posortować tablicę i znaleźć wyraz,
# który występuję najwiekszą ilość razy. Złożoność algorytmu O(nlogn).

from zad3testy import runtests

def podziel(T, start, end):
    x = T[end]
    i = start - 1
    for j in range(start, end):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[end] = T[end], T[i + 1]
    return i + 1

def quicksort(T, start, end):
    if start < end:
        pivot = podziel(T, start, end)
        quicksort(T, start, pivot - 1)
        quicksort(T, pivot + 1, end)
    return T

def strong_string(T):
    n = len(T)
    for i in range(n):
        if T[i][0] > T[i][len(T[i])- 1]:
            T[i] = T[i][::-1]
    quicksort(T, 0, n-1)
    cnt = 0
    best = 0
    for j in range(n - 1):
        if T[j] == T[j+1]:
            cnt += 1
        else:
            best = max(best, cnt)
            cnt = 0
    return best + 1

runtests( strong_string, all_tests = True )
