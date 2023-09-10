from egz2btesty import runtests
from math import inf
# Aby rozwiązać zadanie tworzę tablicę dynamiczną dp o rozmiarze n na m. Wypełniam jej pierwszy wiersz (0-owy indeks)
# odległością pierwszego biurowca od i-tej działki obliczoną zgodnie z założeniami zadania (odlegosc = |xi - xj|).
# Następnie iteruję po każdym biurowcu, po każdej dostępnej działce i po wszystkich sumach długości parkingów poprzedniego biurowca (i-1). 
# Suma odległości do i-tego biurowca z j-tą działką to min z wartośći dp[i][j] oraz sumy odległości do poprzedniego biurowca z k-tą działką + 
# odległość i-tego biurowca od j-tej działki. Pozostało już tylko znaleźć minimalną sumę odległości do n-1 biurowca od i-tej działki.
# Złożonośc algorytmu O(m^3)
def parking(X, Y):
  n = len(X)
  m = len(Y)
  dp =[[inf] * m for _ in range(n)]
  min_distance = inf

  for i in range(m):
    dp[0][i] = abs(X[0] - Y[i])

  for i in range(1, n):
    for j in range(1, m):
      for k in range(i - 1, j):
        dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(X[i] - Y[j]))

  for i in range(m):
    min_distance = min(min_distance, dp[n-1][i])

  return min_distance

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
