def game(heap, moves, to):
    if heap <= 19:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap - 5, moves + 1, to)]
    if heap % 2 == 0:
        if heap % 3 == 0:
            h.append(game(heap // 2, moves + 1, to))
            h.append(game(heap // 3, moves + 1, to))
        else:
            h.append(game(heap // 2, moves + 1, to))
    elif heap % 3 == 0:
        h.append(game(heap // 3, moves + 1, to))
    else:
        h.append(game(heap + 1, moves + 1, to))
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print([s for s in range(1000, 20, -1) if game(s, 0, 3) and not game(s, 0, 1)])
answer1 = 40
answer2 = 43

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2003, f'{answer1} {answer2}', '593697ada77fb63ca3472e9b465e09a6'))