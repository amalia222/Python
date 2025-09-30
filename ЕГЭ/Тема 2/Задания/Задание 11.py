# Решение
from itertools import product, permutations
def f1(x, y, z, w):
    return (x or not y) <= (w == z)

def f2(x, y, z, w):
    return (x or not y) == (w <= z)


for a0, a1, a2, a3, a4, a5 in product((0, 1), repeat=6):
    s = [(0, a0, 0, 0, 0, 0),
         (a1, 1, 1, a2, 0, a3),
         (a4, 0, 0, 0, a5, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f1(i[x], i[y], i[z], i[w]) == i[-2] and f2(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(x, y, z, w)

answer = 'ywxz'

#

import datetime
import hashlib
from tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == '7379de4777f5748aa568b8d0bf8c3795' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 11, 2, result)