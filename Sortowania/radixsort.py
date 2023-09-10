
# niedokonczone
import math
def countingsort(T, k):
    n = len(T)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[T[i]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for i in range(n-1, -1, -1):
        B[C[T[i]] - 1] = T[i]
        C[T[i]] -= 1
    for i in range(n):
        T[i] = B[i]

def getdigit(num, i):
    num /= 10 ** i
    return num % 10

def radixsort(T):
    n = len(T)
    digit = 0
    leng = int(math.log10(n**2-1)) + 1
    for i in range(leng):
        countingsort(T, digit)
        digit += 1