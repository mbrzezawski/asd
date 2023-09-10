from egz3btesty import runtests
from math import inf

def maze( L ):
    n = len(L)
    dp_up_array = [[-1 for _ in range(n)] for _ in range(n)]
    dp_down_array = [[-1 for _ in range(n)] for _ in range(n)]

    if L[0][0] == '.':
        dp_up_array[0][0] = 0 

    for col in range(n):
        for row in range(n):
            if L[row][col] != '#' and row >= 1 and dp_up_array[row - 1][col] != -1:
                dp_up_array[row][col] = max(dp_up_array[row][col], dp_up_array[row - 1][col] + 1)
            if L[row][col] != '#' and col >= 1 and dp_up_array[row][col - 1] != -1:
                dp_up_array[row][col] = max(dp_up_array[row][col], dp_up_array[row][col - 1] + 1)

        for row in range(n - 1, -1, -1):
            if L[row][col] != '#' and row <= n - 2 and dp_down_array[row + 1][col] != -1:
                dp_down_array[row][col] = max(dp_down_array[row][col], dp_down_array[row + 1][col] + 1)
            if L[row][col] != '#' and col >= 1 and dp_down_array[row][col - 1] != -1:
                dp_down_array[row][col] = max(dp_down_array[row][col], dp_down_array[row][col - 1] + 1)

        if col <= n - 2:
            for row in range(n):
                if dp_up_array[row][col] != -1 or dp_down_array[row][col] != -1:
                    dp_up_array[row][col + 1] = max(dp_up_array[row][col], dp_down_array[row][col]) + 1 if L[row][col + 1] == '.' else -1
                    dp_down_array[row][col + 1] = max(dp_up_array[row][col], dp_down_array[row][col]) + 1 if L[row][col + 1] == '.' else -1

    return max(dp_up_array[n - 1][n - 1], dp_down_array[n - 1][n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
