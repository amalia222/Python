def game(heap, moves, to):
    if heap >= 42:
        return moves % 2 == to % 2
    if to == moves:
        return False
    h = [game(heap + 1, moves + 1, to), game(heap + 5, moves + 1, to), game(heap * 3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print([s for s in range(1, 41) if not game(s, 0, 1) and game(s, 0, 3)])