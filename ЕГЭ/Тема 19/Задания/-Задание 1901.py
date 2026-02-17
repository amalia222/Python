def game(heap, moves, to):
    if heap >= 313:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game(heap + 2, moves + 1, to), game(heap + 3, moves + 1, to), game(heap * 2, moves + 1, to)]
    return any(h)

win = [s for s in range(1, 312) if not game(s, 0, 1) and game(s, 0, 2)]
print(sum(win))
print(*win)
answer = 9165

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1901, answer, '9dfcd5e558dfa04aaf37f137a1d9d3e5'))