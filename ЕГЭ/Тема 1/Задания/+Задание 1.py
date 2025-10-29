# Решение
from itertools import permutations

table = '14 15 23 24 25 32 35 36 41 42 47 51 52 53 63 67 74 76'
graph = 'AE EA ED DE DC CD DB BD BC CB CG GC BF FB FG GF GA AG'

for p in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)
answer = 67

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 1, answer, '735b90b4568125ed6c3f678819b6e058'))