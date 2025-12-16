max0 = 0
for x in range(1, 8411):
    maxx = 0
    alg = 29 ** 293 + 29 ** 271 - x
    while alg != 0:
        if alg % 29 == 0:
            maxx += 1
        alg //= 29
    if maxx > max0:
        max0 = maxx
print(max0)