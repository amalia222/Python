for t in range(100, 1000000, 10):
    for y in range(100, 1000000, 10):
        if 900000 >= 250 * t ** 2 + 200 * y ** 2:
            print(t + y)