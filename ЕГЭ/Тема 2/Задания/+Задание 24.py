from itertools import *

def f(x, y, z, w):
    return (x == (y <= z)) and (y == (not(z <= w)))

for a1, a2, a3, a4 in product((0, 1), repeat = 4):
    s = [(0, 0, a1, 0, 1),
         (a2, 0, a3, 0, 1),
         (1, 0, 1, a4, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)

answer = 'wzxy'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 24, answer, 'c5e4e768af58cf865c4006af69319e62'))