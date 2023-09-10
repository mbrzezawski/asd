from zad1testy import runtests
# Maciej Brzeżawski
# Do rozwiązania problemu stowrzyłem tablicę, która przechowuje długości najdłuższego promienia palindromu dla każdego elementu. 
# Przechodząć za pomocą petli for po zadanym wyrazanie wyznaczałem element symetryczny obecnego indeksu względem środka aktualnie badanego palindromu i wykorzystałem zależność, że
# minimalny stopień wartości promienia dla elementu i wynosi T[i_prim] (jeśli, i_prim nie wykracza poza obszar graniczny aktualnie badanego palindromu) lub 
# radius_global - i (jesli i_prim wykracza poza obszar promienia aktualnie badanego palindromu). W dalszej częsci algorytmu pozostało sprawdzić długość akutalnie badanego promienia
#i odpowiednio poszerzać granice globalną. Algorytm ten posiada złożoność stopnia O(n^2).
def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    n = len(s)
    T = [0 for _ in range(n)] # tablica z dlugosciami promienia palindromu dla kazdego elementu 

    radius_global, left, right, best = 0, 0, 0, 0
    
    for i in range(n):
        i_prim = left + right - i # odbicie indeksu i wzgledem srodka akutalnego palindromu 
        
        if i < radius_global: # sprawdzenie czy akutalny indeks mieści się w granicy globalnej
            T[i] = min(T[i_prim], radius_global - i)

        left = i - (T[i] + 1)
        right = i + T[i] + 1

        while right < n and left >=0 and s[left] == s[right]: # sprawdzanie czy następne indeksy są takie same czyli spełniają warunek palindromu
            T[i] += 1
            left -= 1
            right += 1
    
        radius_global = i + T[i]                

        best = max(T[i], best)
    return best * 2 + 1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
