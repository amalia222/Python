def print_matrix(matrix):
    for i in matrix:
        for v in i:
            print(f'{v:4d}', end='')
        print()
    print()

def multiplex_table(n, m):
    return [[i * j for i in range(m)] for j in range(n)]


def chess(n, m):
    return [[(i + j) % 2 for i in range(m)] for j in range(n)]


def andrew_cross(n):
    return [[1 if i == j or n - 1 - i == j else 0 for i in range(n)] for j in range(n)]


def quadrants(n):
    return [[0 if i == j or i + j == n - 1 else 1 if i < j else 2 if j > n - 1 - i else 3 if i > j else 4 for j in range(n)] for i in range(n)]


def nested_rest(n, m):
    return [[min(i, n - 1 - i, j, m - 1 - j) for j in range(m)] for i in range(n)]


def spiral(n, m):
    # Математический способ
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            L = min(i, j, n - 1 - i, m - 1 - j)  # Определяем слой для элемента (i, j)
            base = L * (2 * m + 2 * n - 4 * L)    # Смещение, обусловленное предыдущими оболочками
            # Определяем смещение внутри текущей оболочки
            if i == L:
                offset = j - L
            elif j == m - 1 - L:
                offset = (m - 2 * L - 1) + (i - L)
            elif i == n - 1 - L:
                offset = (m - 2 * L - 1) + (n - 2 * L - 1) + ((m - 1 - L) - j)
            else:
                offset = (m - 2 * L - 1) + (n - 2 * L - 1) + (m - 2 * L - 1) + ((n - 1 - L) - i)
            row.append(base + offset)
        matrix.append(row)
    return matrix