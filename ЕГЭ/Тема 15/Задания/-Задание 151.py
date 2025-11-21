# Решение
for a in range(1, 1000):
    if all(((x & 5160 > 0) or (x & 3650 > 0)) <= ((x & 9545 == 0) <= (x & a > 0)) for x in range(100)):
        print(a)
answer = 34

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 151, answer, '815074618f19008da3c78b95a2f5b964'))