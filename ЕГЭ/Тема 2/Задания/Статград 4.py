from itertools import *


def f(x, y, z, w):
    return y and (not (w) or z == x)


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    s = [(a1, a2, 0, 0, 1),
         (a3, 1, 1, 1, 0),
         (0, a4, a5, 0, 1)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all(f(i[x], i[y], i[z], i[w]) == i[-1] for i in s):
                print(x, y, z, w)

