for a in range(1, 1000):
    if all(((x % a == 0) or ((x in range(200, 250)) <= (x % 55 != 0))) for x in range(1, 1000)):
        print(a)
