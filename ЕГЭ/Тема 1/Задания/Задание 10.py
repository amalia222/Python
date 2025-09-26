from itertools import permutations

table = '13 14 16 23 24 27 28 31 32 34 38 41 42 43 46 56 57 58 61 64 65 67 72 75 76 78 82 83 85 87'
graph = 'АБ БА БВ ВБ БИ ИБ БД ДБ ИД ДИ ИЕ ЕИ ИЖ ЖИ ЖЕ ЕЖ ЖГ ГЖ ЖА АЖ АГ ГА АВ ВА ВД ДВ ДЕ ЕД ГЕ ЕГ'

for i in permutations('АБВГДЕЖИ'):
    n_graph = table
    for j in range(1, 9):
        n_graph = n_graph.replace(str(j), i[j - 1])
    if set(n_graph.split()) == set(graph.split()):
        print(i)

Answer = 14