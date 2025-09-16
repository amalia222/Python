from itertools import permutations

table = '8 8 19 19 11 11 28 28 12 12 20 20 26 26 18 18 29 16 29 16 32 32 15 15 9 9 14 14 17 17'
graph = 'АБ БА БВ ВБ БИ ИБ БД ДБ ИД ДИ ИЕ ЕИ ИЖ ЖИ ЖЕ ЕЖ ЖГ ГЖ ЖА АЖ АГ ГА АВ ВА ВД ДВ ДЕ ЕД ГЕ ЕГ'

for i in permutations('АБВГДЕЖИ'):
    n_graph = table
    for j in range(1, 9):
        n_graph = n_graph.replace(str(j), i[j - 1])
    if set(n_graph.split()) == set(graph.split()):
        print(i)