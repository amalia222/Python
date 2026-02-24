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

print([s for s in range(1, 111) if game(s, 0, 3) and not game(s, 0, 1)])
answer1 = 44
answer2 = 54

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2002, f'{answer1} {answer2}', '92b7c31342bda77734e34f3f8a88b9fa'))