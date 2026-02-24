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
    return any(h)
print([s for s in range(1, 111) if game(s, 0, 2) and not game(s, 0, 1)])
print(game(28, 0, 2))
answer = 54

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1902, answer, 'b53b3a3d6ab90ce0268229151c9bde11'))