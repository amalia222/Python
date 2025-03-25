def find_ways(arr, i, n):
    if n == 0:
        print(*arr)
    for j in range(i, n + 1):
        arr.append(j)
        find_ways(arr, j, n - j)
        del arr[-1]

find_ways([], 1, 4)