def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


for i in range(8996452, 9000000):
    s = prime_factors(i)
    if len(s) == 2:
        print(i, max(s))

