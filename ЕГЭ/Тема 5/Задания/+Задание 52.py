 # Решение
def alg(n):
    binary = bin(n)[2:]
    binary = binary.lstrip('0')
    r1 = binary[1::2].count('1')
    r0 = binary[::2].count('0')
    return max(r0, r1) - min(r0, r1)

n = 1
while True:
    if alg(n) == 5:
        print(n)
        break
    n += 1
answer = 1023

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))