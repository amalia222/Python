from itertools import *

def f(x, y, z, w):
    return ((x <= y) or (y == w)) and ((x or z) == w)

for a1, a2, a3, a4 in product((0, 1), repeat = 4):
    s = [(1, 0, 0, 1, 1),
         (0, a1, a2, 1, 1),
         (a3, 1, 0, a4, 1)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)

answer = 'zyxw'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 27, answer, '9143f4e8bb70c861dcdb22bb9374e909'))