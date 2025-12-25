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

s = []
for n in range(1, 100):
    if alg(n) <= 250:
        s.append(n)
print(max(s))

answer = 26

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))