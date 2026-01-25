def tr(n):
    del3 = ''
    while n != 0:
        del3 += str(n % 3)
        n //= 3
    return del3[::-1]

def alg(n):
    tr_n = tr(n)
    if n % 3 == 0:
        tr_n += tr_n[-2:]
    else:
        tr_n += tr((n % 3) * 5)
    return int(tr_n, 3)

r = []
for n in range(1, 100):
    if alg(n) <= 173:
        r.append(alg(n))
print(max(r))
answer = 162

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 55, answer, '82aa4b0af34c2313a562076992e50aa3'))