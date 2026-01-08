from itertools import *

def f(x, y, z, w):
    return (x == (not y)) <= ((z <= (not w)) and (w <= y))

for a1, a2, a3, a4 ,a5 in product((0, 1), repeat = 5):
    s = [(1, 1, 0, 1, 1),
         (0, a1, 0, a2, 0),
         (a3, a4, a5, 0, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)
answer = 'ywzx'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 25, answer, '1f3ba34df7bed082a628be303ad291df'))