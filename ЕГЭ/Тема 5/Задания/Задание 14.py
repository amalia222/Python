# Решение

def alg(n):
    bin_n = bin(n)[2:]
    bin_n = bin_n + bin(n % 4)
    return int(bin_n, 2)



answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))