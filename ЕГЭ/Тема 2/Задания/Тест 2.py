from itertools import product, permutations


def f1(x, y, z, w):
    return 1 if z or z == w or not (y <= x) else 0


for a0, a1, a2, a3, a4, a5, a6, in product((0, 1), repeat=7):
    s = [(a0, a1, 0, 1, 0),
         (a2, 1, a3, 0, 0),
         (a4, 0, a5, a6, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f1(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(f'x = {x + 1}; y = {y + 1}; z = {z + 1}; w = {w + 1}')
                break