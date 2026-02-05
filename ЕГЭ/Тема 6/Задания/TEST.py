def game(heap, to, moves):
    if heap <= 31:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap - 2, moves + 1, to), game(heap - 5, moves + 1, to), game(heap // 3, moves + 1, to)]
    return any(h)

print(min([s for s in range(32, 150) if not game(s, 0, 1) and game(s, 0, 2)]))