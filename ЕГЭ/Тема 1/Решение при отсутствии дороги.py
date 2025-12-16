from itertools import permutations

table = [
    [0, 17, 14, 0, 29, 35],
    [17, 0, 32, 0, 25, 16],
    [14, 32, 0, 0, 15, 23],
    [0, 0, 0, 0, 18, 34],
    [29, 25, 15, 18, 0, 12],
    [35, 16, 23, 34, 12, 0]
]
graph = 'CF FC FD DF FG GF AF FA BF FB FE EF EB BE BA AB AG GA GD DG DC CD'
connections = 'ABCDEFG' # список узлов графа
graph_connections = set(tuple(sorted((pair[0], pair[1]))) for pair in graph.split()) # множество кортежей типа ("А", "Б")


def calculate_error(permutation):
    # вычисление ошибки в графе
    # чем меньше ошибка тем лучше соответствие
    error = 0
    for i in range(len(connections)):
        for j in range(i + 1, len(connections)):
            # два цикла, чтобы избежать повторных проверок и не сравнивать узел сам с собой
            distance = table[i][j] # получение расстояния
            is_connected = tuple(sorted((permutation[i], permutation[j]))) in graph_connections
            # Проверка на существование связи между permutation[i] и permutation[j]. Возвращают сами узлы
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

# код который основан на длине дорог указанных в графах, появился из-за моего ошибочного мнения