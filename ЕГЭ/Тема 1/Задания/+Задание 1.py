# Решение
from itertools import permutations

table = '14 17 25 26 34 36 41 43 47 52 56 57 62 63 65 71 74 75'
graph = 'АБ БА АВ ВА БГ ГБ БД ДБ ВК КВ ВЕ ЕВ ГД ДГ ДЕ ЕД ЕК КЕ'

for p in permutations('АБВГДЕК'):
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