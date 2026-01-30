def alg(n):
    bin_n = bin(n)[2:]
    bin_n = bin_n[bin_n.index('1') + 1:]
    bin_n = bin_n.lstrip('0')
    if bin_n == '':
        return n - 0
    return n - int(bin_n, 2)

s = []
for n in range(10, 1000):
    s.append(alg(n))
print(len(set(s)))
print(len(s))

answer = 7

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 509, answer, '8f14e45fceea167a5a36dedd4bea2543'))