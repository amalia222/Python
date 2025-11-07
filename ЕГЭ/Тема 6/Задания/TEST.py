from itertools import *
list_val = list(permutations('ХОЧУНАБЮДЖЕТ', 12))
count = 0
count1 = 0
g = list(permutations('ОУАЮЕ', 5))
print(count)
for s in list_val:
    s = ''.join(s)
    for i in g:
        i = ''.join(i)
        if s.count(i) != 0:
            count += 1
    if count == 0:
        count1 += 1
print(count1)
print(len(list_val))