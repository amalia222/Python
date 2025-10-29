# Решение
from itertools import permutations

table = '12 13 14 15 16 17 21 27 31 35 37 41 45 46 51 53 54 61 64 71 72 73'
graph = 'AC CA CG GC CF FC CE EC DC CD CB BC BD DB DE ED EF FE FG GF GA AG'

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