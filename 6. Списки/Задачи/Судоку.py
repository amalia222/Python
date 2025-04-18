def print_matrix(matrix):
    for i in matrix:
        for v in i:
            print(f'{v:4d}', end='')
        print()
    print()


def is_valid_sudoku(n, grid):
    lst = list(range(1, (n ** 2) + 1))
    for row in grid:
        if sorted(row) != lst:
            return False

    for j in range(n ** 2):
        column = [grid[i][j] for i in range(n ** 2)]
        if sorted(column) != lst:
            return False

    for block_row in range(0, n ** 2, n):
        for block_col in range(0, n ** 2, n):
            block = []
            for i in range(block_row, block_row + n):
                for j in range(block_col, block_col + n):
                    block.append(grid[i][j])
            if sorted(block) != lst:
                return False

    return True


n1 = int(input())
grid1 = [list(map(int, input().split())) for i in range(n1 * n1)]
print("YES" if is_valid_sudoku(n1, grid1) else "NO")
