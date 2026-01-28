from itertools import *
graph = 'AB BA AC CA AD DA AE EA AF FA AG GA AH HA BC CB CD DC EF FE FG GF GH HG'
table = '15 18 23 25 31 35 36 45 47 51 52 53 54 56 57 58 63 65 74 75 78 81 85 87'
for p in permutations('ABCDEFGH'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(graph.split()) == set(new_graph.split()):
        print(p)
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 16, answer, '642e92efb79421734881b53e1e1b18b6'))