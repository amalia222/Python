def game(heap, moves, to):
    if heap <= 15:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap - 3, moves + 1, to),
         game(heap - 7, moves + 1, to),
         game(heap // 4, moves + 1, to)]
    return any(h) if (moves + 1) % 2
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1905, answer, 'ea5d2f1c4608232e07d3aa3d998e5135'))