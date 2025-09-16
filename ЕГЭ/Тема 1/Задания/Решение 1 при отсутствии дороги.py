from itertools import permutations

table = '* * * * * * * * * * * * * * * * * * * * * *'
graph = 'CF FC FD DF FG GF AF FA BF FB FE EF EB BE BA AB AG GA GD DG DC CD'
connections = 'ABCDEFG'
graph_connections = set(tuple(sorted((pair[0], pair[1]))) for pair in graph.split())


def calculate_error(permutation):
    error = 0
    for i in range(len(connections)):
        for j in range(i + 1, len(connections)):
            distance = table[i]
            is_connected = tuple(sorted((permutation[i], permutation[j]))) in graph_connections
            if is_connected and distance == 0:
                error += 1
            elif not is_connected and distance != 0:
                error += 1
    return error


best_permutation = None
min_error = float('inf')

for permutation in permutations(connections):

    error = calculate_error(permutation)

    if error < min_error:
        min_error = error
        best_permutation = permutation

if best_permutation:
    index_A = best_permutation.index('A')
    index_G = best_permutation.index('G')