n = int(input())
matr = [[int(i) for i in input().split()] for j in range(n)]
c1 = 0
for i in range(n):
    for j in range(n):
        if i != j and matr[i][j] == matr[j][i]:
            c1 += 1
c2 = n**2 - n
if c1 == c2:
    print('yes')
else:
    print('no')