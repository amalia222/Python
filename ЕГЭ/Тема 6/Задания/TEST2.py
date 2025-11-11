from itertools import *
m = list(permutations('13579', 4))
n = [p for p in product('02468', repeat=4) if p[0] != '0']
for i in m:
    print(*i, end = '\n')