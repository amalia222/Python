# Решение
from itertools import permutations

table = '15 17 24 25 27 34 36 42 43 46 51 52 63 64 68 71 72 78 86 87'
graph = 'AE EA EB BE BF FB BD DB DH HD DG GD GH HG GC CG CF FC FA AF'

for p in permutations('ABCDEFGH'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)
answer = 67

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 1, answer, '735b90b4568125ed6c3f678819b6e058'))