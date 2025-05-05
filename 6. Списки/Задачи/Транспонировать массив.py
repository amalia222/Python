def transpose(matrix):
    return [[matr[j][i] for j in range(len(matr))] for i in range(len(matr[0]))]


def print_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))


n, m = [int(i) for i in input().split()]
matr = [[int(i) for i in input().split()] for j in range(n)]
print_matrix(transpose(matr))