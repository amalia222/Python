def game(heap, moves, to):
    if heap >= 313:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game(heap + 2, moves + 1, to), game(heap + 3, moves + 1, to), game(heap * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


win = [s for s in range(1, 312) if not game(s, 0, 2) and game(s, 0, 4)]

print(*win)
answer = 301

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(21, 2101, answer, '34ed066df378efacc9b924ec161e7639'))