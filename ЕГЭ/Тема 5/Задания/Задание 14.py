# Решение

def alg_14(n):
    binary = bin(n)[2:]
    bi2 = bin(n % 4)[2:]
    r = binary + bi2
    return int(r, 2)


answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))