def print_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))


def multiplex_table(n, m):
    return [[i * j for i in range(m)] for j in range(n)]


def chess(n, m):
    return [[(i + j) % 2 for i in range(m)] for j in range(n)]


def andrey_cross(n):
    return [[1 if i == j or n - 1 - i == j else 0 for i in range(n)] for j in range(n)]


def nested_rest(n, m):
    n, m = int(input()), int(input())
    return [[min(i, n - 1 - i, j, m - 1 - j) for j in range(m)] for i in range(n)]


