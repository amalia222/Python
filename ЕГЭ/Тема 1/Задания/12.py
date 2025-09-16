import hashlib

# Решение

from itertools import permutations

table = '12 13 14 15 17 21 23 24 31 32 37 41 42 45 51 54 56 65 67 71 73 76'
graph = 'AB BA BD DB BE EB BF FB BG GB AG GA AF FA FD DF DC CD CE EC EG GE'

for p in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)

# Ответ
answer = 34
print("Верно" if (hashlib.md5(str(answer).encode()).hexdigest() == 'e369853df766fa44e1ed0ff613f563bd') else "Неверно")
