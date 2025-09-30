# Решение
from itertools import product, permutations
def f(x, y, z, w):
    return ((x == y) <= ((not z) or w)) == (not ((w <= x) or (y <= z)))


for a0, a1, a2, a3, a4 in product((0, 1), repeat=5):
    s = [(0, 1, a0, a1, 1),
         (a2, a3, 1, 0, 1),
         (0, a4, 0, 0, 1)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(x, y, z, w)

answer = 'wzyx'

#

import datetime
import hashlib
from ЕГЭ.tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == 'e0abee87e4ba1de22c6b8cf076c5016b' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 2, 2, result)