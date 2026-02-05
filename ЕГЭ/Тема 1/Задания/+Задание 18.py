from itertools import *
graph = 'ВГ ГВ ВБ БВ БД ДБ БА АБ ГЖ ЖГ ГЕ ЕГ АД ДА ДЕ ЕД ЕЖ ЖЕ'
table = '13 14 16 25 27 31 34 41 43 47 52 56 57 61 65 72 74 75'
for p in permutations('АБВГДЕЖ'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(graph.split()) == set(new_graph.split()):
        print(p)

answer = 7

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 18, answer, '8f14e45fceea167a5a36dedd4bea2543'))