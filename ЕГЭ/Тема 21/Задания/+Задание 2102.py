def game(heap, moves, to):
    if heap >= 112:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    s = [1, heap]
    for i in range(2, heap):
        if heap % i == 0:
            s.append(i)
    h = [game(heap + i, moves + 1, to) for i in s]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print([s for s in range(1, 111) if game(s, 0, 4) and not game(s, 0, 2)])

answer = 43

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(21, 2102, answer, '17e62166fc8586dfa4d1bc0e1742c08b'))