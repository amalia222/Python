# Решение
from itertools import permutations

table = '15 18 23 25 27 32 35 46 47 51 52 53 64 68 72 74 78 81 86 84'
graph = 'АВ ВА АБ БА БД ДБ ДГ ГД ДЕ ЕД ЕГ ГЕ ГВ ВГ ВЖ ЖВ КЖ ЖК АК КА'

for p in permutations('АБВГДЕЖК'):
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