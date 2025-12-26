# Решение
from itertools import *

def f(x, y, z, w):
    return ((x <= y) or (z <= w)) and ((z == y) <= (w == x))

for a0, a1, a2, a3 in product((0, 1), repeat = 4):
    s = [(a0, 1, 0, a1, 0),
         (0, 1, 0, 1, 0),
         (a2, 1, 0, a3, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)
answer = 'yxwz'



from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 21, answer, '1ed5bb3720986c091b8dc2704366e53d'))