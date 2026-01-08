from itertools import *

def f(x, y, z, w):
    return ((not x) and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w)

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat = 7):
    s = [(a1, 1, 0, a2, 1),
         (0, 0, a3, a4, 1),
         (a5, a6, 1, a7, 1)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)
answer = 'xywz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 23, answer, '00e936354216c4a6823136059258f377'))