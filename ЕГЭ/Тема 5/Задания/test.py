for p in range(1, 100):
    for x in range(1, 120):
        for y in range(1, 120):
            if 600 + ((600 * (p // 100)) + ((600 - 5 * x - 5 * y) * (p // 100)) // 2) * 10 == 1740 and x + y == 120:
                print(x, y, p)