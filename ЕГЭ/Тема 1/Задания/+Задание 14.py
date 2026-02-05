from itertools import *
table = '15 16 26 27 29 35 37 38 48 49 51 53 58 61 62 67 72 73 76 83 84 85 92 94'
graph = 'АБ БА БВ ВБ АЕ ЕА АГ ГА ГЕ ЕГ ВК КВ ВД ДВ ДК КД КИ ИК ИЖ ЖИ ЖЕ ЕЖ ГД ДГ'

for p in permutations('АБВГДЕЖИК'):
    new_graph = table
    for i in range(1, 10):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)

answer = 37

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 14, answer, 'a5bfc9e07964f8dddeb95fc584cd965d'))