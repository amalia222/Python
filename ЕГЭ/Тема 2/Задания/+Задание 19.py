# Решение

from itertools import product, permutations


def f(x, y, z, w, u):
    return 1 if ((x <= y) and (z != w)) <= (u == (x or z)) else 0

for a0, a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat = 8):
    s = [(0, a0, 0, 0, 0, 0),
         (0, a1, a2, 0, 0, 0),
         (a3, 0, 0, 0, a4, 0),
         (a5, 0, a6, a7, 0, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w, u in permutations((0, 1, 2, 3, 4)):
            if all([f(i[x], i[y], i[z], i[w], i[u]) == i[-1] for i in s]):
                print(x, y, z, w, u)
                break

answer = "wzyxu"

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 19, answer, 'b83215ff76ddd410e32571919b78d0eb'))