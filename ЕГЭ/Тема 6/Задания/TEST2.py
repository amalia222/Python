"""from itertools import *
list_val = list(permutations('КОБУРА', 6))
count = 0
g = list(permutations('ОУА', 2))
sg = list(permutations('КБР', 2))
for s in list_val:
    s = ''.join(s)
    if all()

print(count)
print(len(list_val))"""
'''from itertools import product, permutations
def f1(x, y, z, w):
    return (x and not y) or (y == z) or not w

for a0, a1, a2, a3 in product((0, 1), repeat = 4):
    s = [(a0, a1, 0, 0, 0),
         (1, 0, a2, 0, 0),
         (1, 0, 1, a3, 0)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f1(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(x, y, z, w)
                break'''
for a in range(2):
    for b in range(2):
        for c in range(2):
            if (b == a or c <= b) and (b == (a or (c <= b))):
                print(a, b, c)