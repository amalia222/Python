n = int(input())
for i in range(n + 1):
        for j in range(n, i, -1):
                print(j, end=' ')
        print()