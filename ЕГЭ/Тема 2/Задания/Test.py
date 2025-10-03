for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x or not y) <= (w == z) and ((x or not y) == (w <= z))):
                    print(x, y, z, w)