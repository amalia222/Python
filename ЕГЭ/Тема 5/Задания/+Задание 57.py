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
s = []
for n in range(1, 1000):
    if alg(n) > 1028:
        s.append(alg(n))
print(min(s))

answer = 1035

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 57, answer, 'a34bacf839b923770b2c360eefa26748'))