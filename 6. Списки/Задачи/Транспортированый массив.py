def print_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))
n, m = [int(i) for i in input().split()]
matr = [[int(i) for i in input().split()] for j in range(n)]

print_matrix(matr)