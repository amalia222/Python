f = [0] * 1_000_000_000
for n in range(1000000000):
    if n == 0:
        f[0] = 0
    elif n % 2 != 0:
        f[n] = f[n - 1] + 1
    else:
        f[n] = f[n // 2]

print(f.count(2))