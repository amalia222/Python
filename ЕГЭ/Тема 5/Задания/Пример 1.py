def tr(n):
    del3 = ''
    while n != 0:
        del3 += str(n % 3)
        n //= 3
    return del3[::-1]

def alg(n):
    tr_n = tr(n)
    if n % 3 == 0:
        tr_n = '1' + tr_n + '02'
    else:
        tr_n = tr_n + tr(n % 3 * 4)
    return int(tr_n, 3)

for n in range(1, 100):
    if alg(n) <= 250:
        print(n)


