def alg(n):
    binary = bin(n)[2:]
    bi2 = bin(n % 4)[2:]
    r = binary + bi2
    return int(r, 2)

n = 1
while True:
    if alg(n) == 999:
        print(n)
        break
    n += 1