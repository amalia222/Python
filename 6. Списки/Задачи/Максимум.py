n, m = [int(i) for i in input().split()]
matr = [[int(i) for i in input().split()] for j in range(n)]
index_i, index_j = 0, 0
curr_max = matr[0][0]
for i in range(n):
    for j in range(m):
        if matr[i][j] > curr_max:
            curr_max = matr[i][j]
            index_i, index_j = i, j
print(index_i + 1, index_j + 1)
