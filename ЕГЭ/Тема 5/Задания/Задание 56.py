def sumdig(n):
    del10 = 0
    while n != 0:
        del10 += n % 10
        n //= 10
    return del10

def alg(n):
    bin_n = bin(n)[2:]
    for i in range(3):
        if sumdig(int(bin_n, 2)) % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
    return int(bin_n, 2)

count = 0
n = 50000000
while n != 500000000:
    if 123456789 <= alg(n) <= 1987654321:
        count += 1
print(count)
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 56, answer, 'f6e1eed3417f1dbf09acd31a21621ef3'))