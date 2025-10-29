# Решение
from itertools import permutations

table = '12 15 18 21 24 36 37 42 48 51 56 63 65 67 73 76 78 81 84 87'
graph = 'AH HA HF FH HB BH BD DB DF FD FE EF EG GE EC CE CG GC AG GA'

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