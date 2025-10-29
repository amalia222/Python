# Решение
from itertools import permutations

table = '15 16 18 23 26 32 34 37 43 46 48 51 57 58 61 62 64 73 75 81 84 85'
graph = 'АБ БА БЕ ЕБ КЕ ЕК КД ДК ДЖ ЖД ЖА АЖ АГ ГА ГБ БГ ГВ ВГ ВЕ ЕВ ВД ДВ'

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