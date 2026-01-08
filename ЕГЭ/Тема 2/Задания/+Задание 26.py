from itertools import *

def f(x, y, z, w):
    return (w == (not(z == y))) and (z == (y <= x))

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat = 7):
    s = [(a1, 0, 0, a2, 1),
         (a3, 0, a4, 0, 1),
         (a5, a6, a7, 0, 1)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)
answer = 'wxzy'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 26, answer, 'd68899696c79e465e2a3547b4dc50435'))