for x in range(1, 100000, 10):
    for y in range(1, 100000, 10):
        if 400 * x ** 2  + 500 * y ** 2  == 7200000:
            print(x, y, x + y)