from egz2atesty import runtests
from math import sqrt
# Maciej Brzeżawski 
# Aby rozwiązać zadanie potrzebuję zmienić wejściową tablice, do danego punktu pod indeksem 'i' dodaje do jego współrzędnych
# długość wektora jaki tworzy ten punkt z punktem (0,0) (twierdzenie pitagorasa). Szukam punktu, którego wektor ma
# największą długość. Pozostało już tylko ostatni raz przejść po tablicy i sprawdzić ile punktów spełnia warunki zadania oraz ma
# długość wektora mniejszą od wcześniej znalezionej największej wartośći. Złożoność algorytmu O(n).
def dominance(P):
  n = len(P)
  for i in range(n):
    vec_lenght = P[i][0] * P[i][0] + P[i][1] * P[i][1] 
    P[i] = P[i][0], P[i][1], sqrt(vec_lenght)
  
  max_vec = -1, -1, -1 
  for i in range(n):
    if P[i][2] > max_vec[2]:
      max_vec = P[i][0], P[i][1], P[i][2]
  
  cnt = 0
  for i in range(n):
    if max_vec[0] > P[i][0] and max_vec[1] > P[i][1] and max_vec[2] > P[i][2]:
      cnt += 1
    
  return cnt

                

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
