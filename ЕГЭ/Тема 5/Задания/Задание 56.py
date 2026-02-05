def alg(n):
    bin_n = bin(n)[2:]
    for i in range(3):
        if bin_n.count('1') % 2 != 0:
            bin_n += '1'
        else:
            bin_n += '0'
    return int(bin_n, 2)
print(alg(17))
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 56, answer, 'f6e1eed3417f1dbf09acd31a21621ef3'))