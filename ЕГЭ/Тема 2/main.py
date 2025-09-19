from itertools import permutations, product


def f1(x, y, z, w):
    return (not (z) == y) <= ((w and not (x)) == (y and x))


for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    table = [
        (x1, 1, 1, 1, 0),
        (1, 1, x2, x3, 0),
        (x4, x5, 0, x6, 0)
    ]
    # Проверка на то, что в таблице не повторяются строки
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, s))) == s[-1] for s in table):
                print(p)
                break


# ----------------------------------

def f1(x, y, z, w):
    return 1 if (not (z) == y) <= ((w and not (x)) == (y and x)) else 0


for a0, a1, a2, a3, a4, a5 in product((0, 1), repeat=6):
    s = [(a0, 1, 1, 1, 0),
         (1, 1, a1, a2, 0),
         (a3, a4, 0, a5, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f1(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(f'x = {x + 1}; y = {y + 1}; z = {z + 1}; w = {w + 1}')
                break
