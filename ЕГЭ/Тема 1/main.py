from itertools import permutations

table = '12 17 21 27 28 34 35 37 43 47 53 57 67 68 71 72 73 74 75 76 78 82 86 87'
graph = 'AB BA AC CA AD DA BC CB CD DC AE EA AF FA AG GA AH HA EF FE FG GF GH HG'

for p in permutations('ABCDEFGH'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)