def fib(n):
    F = [1] * (n+1)
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
print(fib(5))