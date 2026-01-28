def game(heap, moves, to):
    if heap >= 313:
        return moves % 2 == to % 2
    if moves == to:
        return False
    return [game(heap + 2, moves + 1, to), game(heap + 3, moves + 1, to), game(heap * 2, moves + 1, to)]

print()
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1901, answer, '9dfcd5e558dfa04aaf37f137a1d9d3e5'))