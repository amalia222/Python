from itertools import permutations

table = '13 14 17 23 25 26 31 32 34 35 36 37 41 43 52 53 62 63 67 71 73 76'
graph = 'CF FC FD DF FG GF AF FA BF FB FE EF EB BE BA AB AG GA GD DG DC CD'

for i in permutations('ABCDEFG'):
    n_graph = table
    for j in range(1, 8):
        n_graph = n_graph.replace(str(j), i[j - 1])
    if set(n_graph.split()) == set(graph.split()):
        print(i)

answer = 67