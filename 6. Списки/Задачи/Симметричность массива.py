def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matr[i][j] != matr[j][i]:
                return False
    return True


n = int(input())
matr = [[int(i) for i in input().split()] for j in range(n)]

if is_symmetric(matr):
    print('YES')
else:
    print('NO')