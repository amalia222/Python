from itertools import permutations

table = '* * * * * * * * * * * * * * * * * * * * * *'
graph = 'CF FC FD DF FG GF AF FA BF FB FE EF EB BE BA AB AG GA GD DG DC CD'

for i in permutations('ABCDEFG'):
    n_graph = table
    for j in range(1, 8):
        n_graph = n_graph.replace(str(j), i[j - 1])
    if set(n_graph.split()) == set(graph.split()):
        print(i)