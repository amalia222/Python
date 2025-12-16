for a in range(1, 1000):
    if all((y > a) or (152 != 2 * y + 3 * x) or (a < x) for x in range(1000) for y in range(1000)):
        print(a)