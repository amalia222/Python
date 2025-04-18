def print_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))


def minesweeper(n, m, mines):
    grid = [[0] * m for i in range(n)]

    for x, y in mines:
        grid[x][y] = 9

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 9:
                continue
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 9:
                        count += 1
            grid[i][j] = count

    result = []
    for row in grid:
        line = ''
        for cell in row:
            if cell == 9:
                line += '*'
            elif cell == 0:
                line += '.'
            else:
                line += str(cell)
        result.append(line)
    return result

m1, n1, k1 = list(map(int, input().split()))
mines1 = [[int(i) for i in input().split()] for j in range(k1)]
print_matrix(minesweeper(m1, n1, mines1))